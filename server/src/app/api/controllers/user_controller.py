from sqlmodel import Session, select
from schemas.user import UserCreate
from app.models.User import User


def create_user(user_data: UserCreate, session: Session):
    user = User(**user_data.dict())
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


def get_users(session: Session):
    return session.exec(select(User)).all()
