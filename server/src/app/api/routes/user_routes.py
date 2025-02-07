from schemas import UserCreate, UserResponse
from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from db import get_session
from models import User
from typing import List

router = APIRouter(prefix="/users", tags=["Users"])


# Crear usuario
@router.post("/", response_model=UserResponse)
async def create_user(
    user_data: UserCreate,
    session: Session = Depends(get_session)
):
    user = User(**user_data.dict())
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


# Obtener todos los usuarios
@router.get("/", response_model=List[UserResponse])
async def get_users(session: Session = Depends(get_session)):
    users = session.exec(select(User)).all()
    return users
