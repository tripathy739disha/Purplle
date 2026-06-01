"""FastAPI application initialization and configuration."""

from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api import routes
from app.config import settings
from app.database.db import init_db
from app.detection.detector import Detector
from app.detection.tracker import TrackerService
from app.utils.logger import logger


# Global service instances
detector = Detector()
tracker = TrackerService()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manage application startup and shutdown events.

    Args:
        app: FastAPI application instance

    Yields:
        Nothing
    """
    # Startup event
    logger.info(f"Starting {settings.APP_NAME}...")

    try:
        # Initialize database
        init_db()

        # Load YOLO model
        detector.load_model()

        # Initialize tracker
        tracker.initialize()

        logger.info("Application startup completed successfully")

    except Exception as e:
        logger.error(f"Application startup error: {str(e)}")
        raise

    yield

    # Shutdown event
    logger.info("Shutting down application...")


# Create FastAPI application
app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG,
    lifespan=lifespan,
)

# Set service instances for routes
routes.set_detector(detector)
routes.set_tracker(tracker)

# Include routes
app.include_router(routes.router)


@app.get("/")
async def root():
    """Root endpoint.

    Returns:
        Application information
    """
    return {
        "message": f"Welcome to {settings.APP_NAME}",
        "debug": settings.DEBUG,
    }
