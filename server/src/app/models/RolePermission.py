from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime


class RolePermission(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    role_id: int = Field(foreign_key="role.id")
    permission_id: int = Field(foreign_key="permission.id")
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
