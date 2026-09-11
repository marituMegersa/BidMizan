from sqlalchemy import Column, String, DateTime, Float, JSON
import datetime
from app.core.database import Base

class ProcurementBiddingRecord(Base):
    __tablename__ = "procurement_bidding_records"
    id = Column(String, primary_key=True, index=True)
    tender_id = Column(String, nullable=False, index=True)
    fairness_score = Column(Float, default=100.0)
    audit_status = Column(String, default="PASSED")
    sha256_hash = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow, index=True)
