from database.database import engine, Base

# Import all models so SQLAlchemy can detect them
from models.user import User
from models.venue import Venue
from models.event import Event
from models.seat import Seat
from models.offer import Offer
from models.order import Order
from models.ticket import Ticket
from models.refund_request import RefundRequest
from models.support_case import SupportCase
from models.entry_log import EntryLog


def init_db():
    print("Creating tables...")
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully!")


if __name__ == "__main__":
    init_db()