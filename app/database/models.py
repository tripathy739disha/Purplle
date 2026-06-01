"""SQLAlchemy database models."""

from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String

from app.database.db import Base


class Event(Base):
    """Event model for storing detection events."""

    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    event_type = Column(String, nullable=False, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow, nullable=False, index=True)

    def __repr__(self) -> str:
        """String representation of Event."""
        return (
            f"<Event(id={self.id}, event_type='{self.event_type}', "
            f"timestamp={self.timestamp})>"
        )
