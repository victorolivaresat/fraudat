from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime


class ModulePermission(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    module_id: int = Field(foreign_key="module.id")
    permission_id: int = Field(foreign_key="permission.id")
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
