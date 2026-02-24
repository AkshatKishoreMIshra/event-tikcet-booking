from datetime import datetime
from decimal import Decimal
from typing import Optional
from sqlalchemy import DateTime, ForeignKey, DECIMAL
from sqlalchemy.orm import Mapped, mapped_column
from database.database import Base

class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    offer_id: Mapped[Optional[int]] = mapped_column(ForeignKey("offers.id"), nullable=True)
    total_amount: Mapped[Decimal] = mapped_column(DECIMAL)
    discount_amount: Mapped[Decimal] = mapped_column(DECIMAL)
    final_amount: Mapped[Decimal] = mapped_column(DECIMAL)
    payment_mode: Mapped[str]
    order_status: Mapped[str]
    booking_time: Mapped[datetime] = mapped_column(default=datetime.utcnow)