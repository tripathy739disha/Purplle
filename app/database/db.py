"""Database connection and session management."""

from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.config import settings
from app.utils.logger import logger

# Create Base class for models
Base = declarative_base()

# Ensure data directory exists
data_dir = Path("data")
data_dir.mkdir(exist_ok=True)

# Create database engine
engine = create_engine(
    settings.DATABASE_URL,
    connect_args={"check_same_thread": False},  # Required for SQLite
    echo=settings.DEBUG,
)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    """Dependency for FastAPI to get database session.

    Yields:
        Database session
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    """Initialize database by creating all tables."""
    try:
        logger.info("Initializing database...")
        Base.metadata.create_all(bind=engine)
        logger.info(f"Database initialized at {settings.DATABASE_URL}")
    except Exception as e:
        logger.error(f"Database initialization error: {str(e)}")
        raise
