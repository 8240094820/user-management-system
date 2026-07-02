from sqlalchemy.orm import Query
from sqlalchemy.sql import func
from application.models.users import UserAccess
from application.models.role import Role
from sqlalchemy.orm import Query



# For count
def get_count(query: Query) -> int:
    count_query = query.statement.with_only_columns(func.count(1))
    count: int = query.session.execute(count_query).scalar()
    return count

# For page limit
def set_limit_offset(query: Query, page: int = 0, page_size: int = 10) -> Query:
    if page_size:
        query = query.limit(page_size)
    if page:
        query = query.offset((page - 1) * page_size)
    return query

# For sort in Users
def set_sort_order_user(query: Query, sort_column: str, sort_order: str) -> Query:
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


