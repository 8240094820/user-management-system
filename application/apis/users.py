from flask import Blueprint, request, abort, Response
from sqlalchemy import or_
import logging
from werkzeug.security import generate_password_hash
from sqlalchemy.orm import Session
from application.models.database import DB_SESSION
from application.models.users import UserAccess
from application.models.role import Role
from typing import Dict, Any, List, Optional, Tuple
from application.utils.common_utils import get_count, set_limit_offset, set_sort_order_user
from application.models.users import UserAccess, format_as_get_user_list_response
from sqlalchemy.orm import Query
from application.utils.enums import SortOrder, SortColumn

session: Session = DB_SESSION
USER_API: Blueprint = Blueprint('user_management_api', __name__)

def get_blueprint() -> Blueprint:
    return USER_API


# Create Users
@USER_API.route('/users', methods=['POST'])
def create_user() -> Response:
    data: Dict[str, Any] = request.get_json()
    name: Optional[str] = data.get('name')
    email: Optional[str] = data.get('email')
    password: Optional[str] = data.get('password')
    role_name: Optional[str] = data.get('role')

    if not all([name, email, password, role_name]):
        abort(400, 'Missing fields')

    existing_user: Optional[UserAccess] = session.query(UserAccess).filter_by(email=email).first()
    if existing_user:
        abort(409, 'User already exists')

    role: Optional[Role] = session.query(Role).filter_by(role_name=role_name).first()
    if not role:
        abort(400, 'Invalid role')

    new_user = UserAccess(
        name=name,
        email=email,
        password_hash=generate_password_hash(password),
        active=True,
        role_id=role.id
    )
    session.add(new_user)
    session.commit()

    return (
    {
        "message": "User created successfully",
        "user_id": new_user.id
    },
    201
)

# Update user
@USER_API.route('/users/<int:user_id>', methods=['PATCH'])
def update_user(user_id) -> Response:
    user: Optional[UserAccess] = session.query(UserAccess).filter_by(id=user_id).first()
    if not user:
        abort(404, 'User not found')

    data: Dict[str, Any] = request.get_json()
    user.name = data.get('name', user.name)
    user.email = data.get('email', user.email)
    if 'password' in data:
        user.password_hash = generate_password_hash(data['password'])
    if 'active' in data:
        user.active = data['active']
    if 'role' in data:
        role: Optional[Role] = session.query(Role).filter_by(role_name=data['role']).first()
        if role:
            user.role_id = role.id

    session.commit()
    return ({'message': 'User updated successfully'})

# List of all users
@USER_API.route('/users', methods=['GET'])
def list_users() -> Response:
    users: List[Tuple[UserAccess, Role]] = session.query(UserAccess, Role).join(Role, UserAccess.role_id == Role.id).all()
    user_list: List[Dict[str,Any]] = [{
        'id': user.id,
        'name': user.name,
        'email': user.email,
        'active': user.active,
        'role': role.role_name
    } for user, role in users]
    return ({'data': user_list})

# Delete user
@USER_API.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id) -> Response:
    user: Optional[UserAccess] = session.query(UserAccess).filter_by(id=user_id).first()
    if not user:
        abort(404, 'User not found')

    session.delete(user)
    session.commit()
    return ({'message': 'User deleted successfully'})

# self operation
@USER_API.route('/users/me', methods=['GET', 'PATCH'])
def get_self_user() -> Response:
    current_user: Dict[str, Any] = request.user
    user: Optional[UserAccess] = session.query(UserAccess).filter_by(id=current_user['user_id']).first()
    if not user:
        abort(404, 'User not found')

    if request.method == 'PATCH':
        data = request.get_json()
        if 'name' in data:
            user.name = data['name']
        if 'email' in data:
            user.email = data['email']
        if 'password' in data:
            user.password_hash = generate_password_hash(data['password'])
        session.commit()
        return ({'message': 'Profile updated successfully'})

    role: Optional[Role] = session.query(Role).filter_by(id=user.role_id).first()

    return ({
        'id': user.id,
        'name': user.name,
        'email': user.email,
        'active': user.active,
        'role': role.role_name
    })

# sort, search, filter, pagination operation
@USER_API.route('/getUsersList', methods=['GET'])
def get_users_list() -> Response:
    # ---- Validate inputs before main try ----
    page_limit: int = int(request.args.get('page_limit', 10))
    page_number: int = int(request.args.get('page_number', 0))
    search_string: Optional[str] = request.args.get('search_string')

    # Validate sort_column
    sort_column_row: Optional[str] = request.args.get('sort_column')
    sort_column: Optional[SortColumn] = None
    if sort_column_row:
        try:
            sort_column = SortColumn(sort_column_row)
        except ValueError:
            abort(400, description="Invalid sort_column. Allow only: Name, Email, Role, Status")

    # Validate sort_order
    sort_order_row: str = request.args.get('sort_order', 'asc')
    try:
        sort_order: SortOrder = SortOrder(sort_order_row.lower())
    except ValueError:
        abort(400, description="Invalid sort_order. Allow only: 'asc' or 'desc'.")

    # ---- Main logic ----
    try:
        # Search Filter List
        search_filter = []
        if search_string:
            search_filter.append(UserAccess.name.ilike(f'%{search_string}%'))
            search_filter.append(UserAccess.email.ilike(f'%{search_string}%'))
            search_filter.append(Role.role_name.ilike(f'%{search_string}%'))

        # Base Query
        user_list_query: Query = session.query(UserAccess, Role) \
            .join(Role, UserAccess.role_id == Role.id) \
            .filter(or_(*search_filter)) 
        
        # Count total records
        total_records: int = get_count(user_list_query)

        # Sorting
        if sort_column:
            user_list_query = set_sort_order_user(user_list_query, sort_column.value, sort_order.value)
        else:
            user_list_query = user_list_query.order_by(UserAccess.id.desc())

        # Pagination
        user_list = set_limit_offset(user_list_query, page_number, page_limit)

        result: Dict[str, Any] = {
            'data': [format_as_get_user_list_response(user) for user in user_list],
            'total_records': total_records
        }
        return (result)

    except Exception as e:
        if '401 Unauthorized' in str(e):
            abort(401)
        elif '400 Bad request' in str(e):
            abort(400)
        logging.error(f"endpoint: {request.endpoint} - {e}", exc_info=True)
        abort(500)