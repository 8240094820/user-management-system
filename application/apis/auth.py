from flask import Blueprint, request, abort, Response
from werkzeug.security import check_password_hash
from sqlalchemy.orm import Session
from application.models.database import DB_SESSION
from application.models.users import UserAccess
from application.models.role import Role
from application.services.auth_service import create_token
from application.services.logging_service import logging
from application.conf.config import get_config


CONFIG = get_config()
session: Session = DB_SESSION

AUTH_API: Blueprint = Blueprint('auth_api', __name__)
def get_blueprint() -> Blueprint:
    return AUTH_API

@AUTH_API.route('/login', methods=['POST'])
def login() -> Response:
    request_data: dict[str, str] = request.get_json()
    email: str = request_data.get('email')
    password: str = request_data.get('password')

    if not (email and password):
        abort(400, "Email and password are required.")

        # Fetch User & Role from DB
    try:
        user_details = session.query(UserAccess, Role) \
            .join(Role, Role.id == UserAccess.role_id) \
            .filter(UserAccess.email == email) \
            .filter(UserAccess.active.is_(True)).first()
    except Exception as e:
        logging.error(f"DB error: {e}")
        abort(500)
    
    if not user_details:
        abort(403, "Invalid email or inactive user.")

    user: UserAccess
    role: Role
    user, role = user_details

    if not check_password_hash(user.password_hash, password):
        abort(403, "Invalid password.")
    
    try:
        meta_data = {'user_id': user.id, 'roles': [role.role_name]}
        token: str | None = create_token(CONFIG.AUTH_TOKEN_EXPIRY_TIME_IN_SEC, 'api_auth_key', meta_data)
    except Exception as e:
        logging.error(f"Token generation failed: {e}")
        abort(500)

    if not token:
        abort(500)

    return ({'status': 'Success', 'auth_token': token})