# app/db/postgres.py
from databases import Database
from sqlmodel import create_engine, MetaData
from ..core.config import os_getenv




DATABASE_URL = os_getenv("DATABASE_URL")

# Async Database instance
database = Database(DATABASE_URL)
metadata = MetaData()

# Optional: SQLAlchemy engine (for migrations or sync operations)
engine = create_engine(DATABASE_URL.replace("+asyncpg", ""))  # sync engine
