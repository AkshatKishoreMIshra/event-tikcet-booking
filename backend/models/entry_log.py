from datetime import datetime
from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from database.database import Base

class EntryLog(Base):
    __tablename__ = "entry_logs"

    id: Mapped[int] = mapped_column(primary_key=True)
    ticket_id: Mapped[int] = mapped_column(ForeignKey("tickets.id"))
    entry_time: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    status: Mapped[str]