from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
import datetime
from app.db.base import Base

class TenderCenter(Base):
    __tablename__ = "tender_centers"

    id = Column(String, primary_key=True, index=True)
    center_name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    authority_id = Column(String, ForeignKey("procurement_authorities.id"), nullable=True, index=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    authority = relationship("ProcurementAuthority", back_populates="centers")
    auditors = relationship("ProcurementAuditor", back_populates="center", cascade="all, delete-orphan")
