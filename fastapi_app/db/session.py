import asyncio

from sqlalchemy.ext.asyncio import (
    async_scoped_session,
    async_sessionmaker,
    create_async_engine, AsyncSession,
)

from fastapi_app.core.config import config


async_engine = create_async_engine(
    config.DatabaseConfig.database_url,
    pool_pre_ping=True,
    echo=True,
)

AsyncSessionLocal = async_sessionmaker(
    bind=async_engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)

async_db_session = async_scoped_session(
    AsyncSessionLocal,
    scopefunc=asyncio.current_task,
)

async def get_db() -> AsyncSession:
    async with async_db_session() as session:
        try:
            yield session
        finally:
            await session.close()