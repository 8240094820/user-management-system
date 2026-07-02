import os

class Config:
    SECRET_KEY: str = os.getenv("SECRET_KEY", "any-random-secret")
    SQLALCHEMY_DATABASE_URI: str = os.environ.get('DATABASE_URI', 'sqlite:///test_local.db')
    JWT_PRIVATE_KEY_PATH: str = os.path.join(os.getcwd(), 'application', 'conf', 'private.pem')
    JWT_PUBLIC_KEY_PATH: str = os.path.join(os.getcwd(), 'application', 'conf', 'public.pem')
    AUTH_TOKEN_EXPIRY_TIME_IN_SEC: int = int(os.getenv('AUTH_TOKEN_EXPIRY_TIME_IN_SEC', 1800))
    BASE_URI: str = '/api/v1'
    CORS_DOMAINS  = ["*"]
    DEBUG: bool = os.getenv('DEBUG') == '1'


def get_config() -> Config:
    return Config