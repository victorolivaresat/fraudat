from pydantic import BaseModel, EmailStr
from datetime import datetime


class UserCreate(BaseModel):
    firstname: str
    lastname: str
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    firstname: str
    lastname: str
    email: str
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
