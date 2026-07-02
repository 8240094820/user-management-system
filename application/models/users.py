from dataclasses import dataclass
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from application.models.database import DB_SESSION
from sqlalchemy.orm import Query
from application.models.role import Role
from typing import Dict, Any, Tuple

MODEL = declarative_base(name='MODEL')
MODEL.query = DB_SESSION.query_property()

@dataclass
class UserAccess(MODEL):
    __tablename__ = 'user_access'
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    name: str = Column(String(255), nullable=False)
    email: str = Column(String(255), unique=True, nullable=False)
    password_hash: str = Column(String(255), nullable=False)
    active: bool = Column(Boolean, default=True)
    role_id: int = Column(Integer, nullable=False) 


def set_sort_order(query: Query, sort_column: str, sort_order: str) -> Query:
    if sort_column == 'Name' and sort_order == 'asc':
        query = query.order_by(UserAccess.name)
    elif sort_column == 'Email' and sort_order == 'asc':
        query = query.order_by(UserAccess.email)
    elif sort_column == 'Email':
        query = query.order_by(UserAccess.email.desc())
    elif sort_column == 'Role' and sort_order == 'asc':
        query = query.order_by(Role.role_name)
    elif sort_column == 'Role':
        query = query.order_by(Role.role_name.desc())
    elif sort_column == 'Status' and sort_order == 'asc':
        query = query.order_by(UserAccess.active.desc())
    elif sort_column == 'Status':
        query = query.order_by(UserAccess.active.desc())

    return query


def format_as_get_user_list_response(data_fetched: Tuple['UserAccess', Role]) -> Dict[str, Any]:
    response = {
        'user_id': data_fetched[0].id,
        'name': data_fetched[0].name,
        'email': data_fetched[0].email,
        'role': data_fetched[1].role_name,
        'status': data_fetched[0].active
    }
    return response