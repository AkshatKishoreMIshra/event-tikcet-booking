from datetime import datetime, date
from decimal import Decimal
from sqlalchemy import Date, Boolean, DECIMAL, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from database.database import Base

class Offer(Base):
    __tablename__ = "offers"

    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[str] = mapped_column(unique=True)
    discount_percent: Mapped[Decimal] = mapped_column(DECIMAL)
    max_discount_amount: Mapped[Decimal] = mapped_column(DECIMAL)
    expiry_date: Mapped[date]
    is_active: Mapped[bool]
    usage_limit: Mapped[int]
    used_count: Mapped[int]
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)