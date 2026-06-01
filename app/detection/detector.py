"""YOLO object detection module."""

from pathlib import Path

from ultralytics import YOLO

from app.config import settings
from app.utils.logger import logger


class Detector:
    """YOLO model wrapper for object detection."""

    def __init__(self, model_path: str = settings.YOLO_MODEL_PATH):
        """Initialize detector with model path.

        Args:
            model_path: Path to YOLOv8 model file
        """
        self.model_path = model_path
        self.model = None
        self.logger = logger

    def load_model(self) -> bool:
        """Load YOLO model from disk.

        Returns:
            True if model loaded successfully, False otherwise
        """
        try:
            if not Path(self.model_path).exists():
                self.logger.warning(
                    f"Model path does not exist: {self.model_path}. "
                    "Model will be downloaded on first load."
                )

            self.logger.info(f"Loading YOLO model from {self.model_path}...")
            self.model = YOLO(self.model_path)
            self.logger.info("YOLO model loaded successfully")
            return True

        except Exception as e:
            self.logger.error(f"Failed to load YOLO model: {str(e)}")
            return False

    def is_loaded(self) -> bool:
        """Check if model is loaded.

        Returns:
            True if model is loaded, False otherwise
        """
        return self.model is not None

    def detect(self, frame):
        """Run object detection on a frame.

        Args:
            frame: Input frame/image for detection

        Returns:
            Detection results or None if model not loaded
        """
        if not self.is_loaded():
            self.logger.error("Model not loaded. Call load_model() first.")
            return None

        try:
            results = self.model(frame)
            return results

        except Exception as e:
            self.logger.error(f"Detection error: {str(e)}")
            return None
