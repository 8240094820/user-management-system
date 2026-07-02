from dataclasses import dataclass
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from application.models.database import DB_SESSION


MODEL = declarative_base(name='MODEL')
MODEL.query = DB_SESSION.query_property()

@dataclass
class Role(MODEL):
    __tablename__ = 'role'
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    role_name: str = Column(String(100), unique=True, nullable=False)
