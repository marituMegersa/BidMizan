from sqlalchemy import Column, String, DateTime
import datetime
from app.db.base import Base

class TenderCenter(Base):
    __tablename__ = "tender_centers"

    id = Column(String, primary_key=True, index=True)
    center_name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
