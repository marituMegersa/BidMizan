from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
import datetime
from app.db.base import Base

class ProcurementAuditor(Base):
    __tablename__ = "procurement_auditors"

    id = Column(String, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    badge_number = Column(String, nullable=False)
    center_id = Column(String, ForeignKey("tender_centers.id"), nullable=True, index=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    center = relationship("TenderCenter", back_populates="auditors")
