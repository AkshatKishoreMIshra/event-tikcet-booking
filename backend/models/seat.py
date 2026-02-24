from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column
from database.database import Base

class Seat(Base):
    __tablename__ = "seats"

    id: Mapped[int] = mapped_column(primary_key=True)
    seat_number: Mapped[str]
    status: Mapped[str]
    event_id: Mapped[int] = mapped_column(ForeignKey("events.id"))

    __table_args__ = (
        UniqueConstraint("event_id", "seat_number", name="unique_seat_per_event"),
    )