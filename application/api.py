from flask import Flask, make_response, Response, jsonify, abort, request
from application.services.auth_service import  get_meta_data_from_header
from application.apis import auth, users
from flask_cors import CORS
from application.models.database import DB_SESSION
from application.conf.config import get_config


app: Flask = Flask(__name__)

CONFIG = get_config()
BASE_URI: str = CONFIG.BASE_URI

CORS(app, resources={r'/api/*': {'origins': CONFIG.CORS_DOMAINS}})

app.register_blueprint(users.get_blueprint(), url_prefix=BASE_URI)
app.register_blueprint(auth.get_blueprint(), url_prefix=BASE_URI)

PUBLIC_ENDPOINTS: set[str] = {
    'auth_api.login',
}

# Staff-restricted Endpoints (Admin only)
STAFF_BLOCKED_ENDPOINTS: set[str] = {
    'user_management_api.list_users',
    'user_management_api.create_user',
    'user_management_api.update_user',
    'user_management_api.delete_user',
    'user_management_api.get_users_list',
    
    
}

@app.before_request
def require_authorization() ->Response:
    """
    Middleware to handle Auth, RBAC, and request logging
    """
    #print(f"Request Endpoint: {request.endpoint}")
    #print(f"Request URL: {request.url}")
    #print(f"Request Method: {request.method}")
    #print(f"View Function Mapping: {app.view_functions}")
    #print(f"Request Endpoint: {request.endpoint}")
    if request.endpoint in PUBLIC_ENDPOINTS:
        return None  # Public endpoints don’t need auth

    if 'api/v1/' in request.url and request.method != 'OPTIONS':
        # Extract user meta data from Authorization header
        meta_data = get_meta_data_from_header()

        if not meta_data:
            app.logger.warning(f"Unauthorized request at {request.endpoint}")
            abort(401, 'Invalid or expired token')

        user = meta_data.get('user', {})
        user_id = user.get('user_id')
        roles: list[str] = user.get('roles', [])

        # Validate token payload
        if not user_id:
            abort(401, 'Invalid Token Payload')

    

        # Attach user_id and roles to request object 
        request.user = {
            'user_id': user_id,
            'roles': roles
        }
        # RBAC: Prevent Staff from accessing Admin-only endpoints
        if 'Staff' in roles and request.endpoint in STAFF_BLOCKED_ENDPOINTS:
            abort(403, 'Forbidden for Staff role')


    return None

@app.teardown_request
def remove_db_session(exception) -> None:
    """Always remove DB session after request"""
    DB_SESSION.remove()



# ----------- Error Handlers ----------- #
@app.errorhandler(400)
def handle_400_error(error: Exception) -> Response:
    return make_response(jsonify({'errors': [{'status': '400', 'detail': str(error)}]}), 400)

@app.errorhandler(401)
def handle_401_error(error: Exception) -> Response:
    return make_response(jsonify({'errors': [{'status': '401', 'detail': str(error)}]}), 401)

@app.errorhandler(403)
def handle_403_error(error: Exception) -> Response:
    return make_response(jsonify({'errors': [{'status': '403', 'detail': str(error)}]}), 403)

@app.errorhandler(404)
def handle_404_error(error: Exception) -> Response:
    return make_response(jsonify({'errors': [{'status': '404', 'detail': str(error)}]}), 404)

@app.errorhandler(409)
def handle_409_error(error: Exception) -> Response:
    return make_response(jsonify({'errors': [{'status': '409', 'detail': str(error)}]}), 409)

@app.errorhandler(410)
def handle_410_error(error: Exception) -> Response:
    return make_response(jsonify({'errors': [{'status': '410', 'detail': str(error)}]}), 410)

@app.errorhandler(429)
def handle_429_error(error: Exception) -> Response:
    return make_response(jsonify({'errors': [{'status': '429', 'detail': str(error)}]}), 429)

@app.errorhandler(500)
def handle_500_error(error: Exception) -> Response:
    return make_response(jsonify({'errors': [{'status': '500', 'detail': 'Internal Server Error'}]}), 500)
