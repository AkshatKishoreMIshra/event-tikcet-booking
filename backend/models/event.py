from datetime import datetime, date
from decimal import Decimal
from sqlalchemy import Date, DateTime, ForeignKey, DECIMAL
from sqlalchemy.orm import Mapped, mapped_column
from database.database import Base

class Event(Base):
    __tablename__ = "events"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    category: Mapped[str]
    event_date: Mapped[date]
    ticket_price: Mapped[Decimal] = mapped_column(DECIMAL)
    max_tickets_per_user: Mapped[int]
    status: Mapped[str]
    venue_id: Mapped[int] = mapped_column(ForeignKey("venues.id"))
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)