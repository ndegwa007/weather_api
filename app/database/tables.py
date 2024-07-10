from app.models import Base
from app.database.engine import engine
from loguru import logger

async def create_tables():
    logger.info("Starting table creation")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    logger.info("Tables created successfully")