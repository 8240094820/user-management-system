import jwt
from datetime import datetime, timedelta
from flask import request
import os
from typing import Optional, Dict, Any
from application.services.logging_service import logging 

# Load private & public keys from files
def load_private_key() -> str:
    with open(os.path.join(os.getcwd(), 'application', 'conf', 'private.pem'), 'r') as f:
        return f.read()

def load_public_key() -> str:
    with open(os.path.join(os.getcwd(), 'application', 'conf', 'public.pem'), 'r') as f:
        return f.read()

# Create JWT Token
def create_token(timeout, audience, meta_data):
    try:
        now: datetime = datetime.utcnow()
        expiry_time: datetime = now + timedelta(seconds=timeout)

        payload = {
            'iat': now,
            'exp': expiry_time,
            'aud': audience,
            'user': meta_data
        }

        private_key: str = load_private_key()
        encoded: str = jwt.encode(payload, private_key, algorithm='RS256')
        return encoded
    except Exception as e:
        logging.error(f"Token creation failed: {e}", exc_info=True)
        return None

# Decode and Verify JWT Token
def decode_token(token: str, audience: str):
    try:
        public_key: str = load_public_key()
        decoded: Dict[str, Any] = jwt.decode(token, public_key, algorithms=['RS256'], audience=audience)
        return decoded
    except jwt.ExpiredSignatureError:
        logging.warning("Token expired")
        return None
    except jwt.InvalidTokenError as e:
        logging.error(f"Invalid token: {e}", exc_info=True)
        return None
    except Exception as e:
        logging.error(f"Unexpected error while decoding token: {e}", exc_info=True)
        return None

# Get Meta Data from Authorization Header
def get_meta_data_from_header():
    try:
        auth_header: Optional[str] = request.headers.get('Authorization')
        if not auth_header:
            return None
        auth_token: str = auth_header.split()[-1]  # Extract token from "Bearer <token>"
        decoded_data: Optional[Dict[str, Any]] = decode_token(auth_token, 'api_auth_key')
        if not decoded_data:
            return None
        return decoded_data
    except Exception as e:
        logging.error(f"Error in get_meta_data_from_header: {e}", exc_info=True)
        return None

# Get current User ID from token
def get_current_user_id():
    try:
        meta_data: Optional[Dict[str, Any]] = get_meta_data_from_header()
        if not meta_data:
            return None
        user_id: Optional[int] = meta_data.get('user', {}).get('user_id')
        return user_id
    except Exception as e:
        logging.error(f"Error in get_current_user_id: {e}", exc_info=True)
        return None


# Get current User Role from token
def get_current_user_role():
    try:
        meta_data: Optional[Dict[str, Any]] = get_meta_data_from_header()
        if not meta_data:
            return None
        roles: Optional[list[str]] = meta_data.get('user', {}).get('roles')
        return roles[0] if roles else None
    except Exception as e:
        logging.error(f"Error in get_current_user_role: {e}", exc_info=True)
        return None