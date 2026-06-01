"""API routes for health checks and service status."""

from fastapi import APIRouter

router = APIRouter()

# Service instances (will be set by main.py)
detector_instance = None
tracker_instance = None


def set_detector(detector):
    """Set detector instance."""
    global detector_instance
    detector_instance = detector


def set_tracker(tracker):
    """Set tracker instance."""
    global tracker_instance
    tracker_instance = tracker


@router.get("/health")
async def health_check():
    """Health check endpoint.

    Returns:
        Status of the application
    """
    return {"status": "healthy"}


@router.get("/detector/status")
async def detector_status():
    """Check YOLO detector status.

    Returns:
        YOLO model loading status
    """
    is_loaded = False
    if detector_instance:
        is_loaded = detector_instance.is_loaded()

    return {"yolo_loaded": is_loaded}


@router.get("/tracker/status")
async def tracker_status():
    """Check ByteTrack tracker status.

    Returns:
        Tracker initialization status
    """
    is_ready = False
    if tracker_instance:
        is_ready = tracker_instance.is_ready()

    return {"tracker_ready": is_ready}
