from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import relationship
import datetime
from app.db.base import Base

class ProcurementAuthority(Base):
    __tablename__ = "procurement_authorities"

    id = Column(String, primary_key=True, index=True)
    authority_name = Column(String, nullable=False)
    jurisdiction = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    centers = relationship("TenderCenter", back_populates="authority", cascade="all, delete-orphan")
