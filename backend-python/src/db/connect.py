from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker
from typing import AsyncGenerator
from src.config import settings
from sqlmodel import SQLModel

# Obtener la URL de la base de datos desde las variables de entorno
database_url = (
    f"postgresql+asyncpg://{settings.DB_USER}:{settings.DB_PASSWORD}@"
    f"{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
)


async_engine = create_async_engine(url=database_url, echo=True)


async def init_db():
    """Create the database tables"""
    async with async_engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    """Dependency to provide the session object"""
    async_session = sessionmaker(
        bind=async_engine, class_=AsyncSession, expire_on_commit=False
    )

    async with async_session() as session:
        yield session
