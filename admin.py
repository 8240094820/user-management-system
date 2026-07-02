from application.api import app
from application.models.database import DB_SESSION
from application.models.users import UserAccess
from application.models.role import Role
from werkzeug.security import generate_password_hash
from sqlalchemy.orm import Session
from sqlalchemy.engine import Engine
from typing import Optional


with app.app_context():
    session: Session = DB_SESSION
    engine: Engine = DB_SESSION.bind

    # Ensure that tables are created
    Role.__table__.create(bind=engine, checkfirst=True)
    UserAccess.__table__.create(bind=engine, checkfirst=True)

    # Insert only 'Admin' Role if not exist
    admin_role: Optional[Role] = session.query(Role).filter_by(role_name='Admin').first()
    if not admin_role:
        admin_role = Role(role_name='Admin')
        session.add(admin_role)

    # Add Staff Role if not exist
    staff_role: Optional[Role] = session.query(Role).filter_by(role_name='Staff').first()
    if not staff_role:
        staff_role = Role(role_name='Staff')
        session.add(staff_role)

    session.commit()
    print("Roles ensured in DB.")

    # Insert Admin User if not exist
    admin_email: str = "admin123@gmail.com"
    existing_admin: Optional[UserAccess] = session.query(UserAccess).filter_by(email=admin_email).first()

    if not existing_admin:
        admin_user: UserAccess = UserAccess(
            name='Admin User',
            email=admin_email,
            password_hash=generate_password_hash('admin123'),
            active=True,
            role_id=admin_role.id  
        )
        session.add(admin_user)
        session.commit()
        print("Admin user created.")
    else:
        print("Admin user already exists.")

