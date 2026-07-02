from application.conf.config import get_config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


CONFIG_PROP = get_config()

CONNECTION_STRING = CONFIG_PROP.SQLALCHEMY_DATABASE_URI

# Create SQLAlchemy Engine
ENGINE = create_engine(CONNECTION_STRING,
                        echo=CONFIG_PROP.DEBUG,
                        pool_recycle=900,
                        pool_pre_ping=True
                        )

DB_SESSION = scoped_session(
                            sessionmaker(
                                autocommit=False,
                                autoflush=False,
                                bind=ENGINE
                            )
                        )