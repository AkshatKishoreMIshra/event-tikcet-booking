from datetime import datetime
from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from database.database import Base

class Ticket(Base):
    __tablename__ = "tickets"

    id: Mapped[int] = mapped_column(primary_key=True)
    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"))
    seat_id: Mapped[int] = mapped_column(ForeignKey("seats.id"), unique=True)
    ticket_code: Mapped[str] = mapped_column(unique=True)
    status: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)