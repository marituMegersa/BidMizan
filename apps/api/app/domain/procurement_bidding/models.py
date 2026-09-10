from sqlalchemy import Column, String, Boolean, DateTime, Float, Integer, JSON
import datetime
from app.db.base import Base

class ProcurementBiddingRecord(Base):
    __tablename__ = "procurement_bidding_records"

    id = Column(String, primary_key=True, index=True)

    tender_id = Column(String, nullable=False, index=True)
    vendor_name = Column(String, nullable=False)
    bid_amount = Column(Float, nullable=False)
    compliance_score = Column(Float, default=0.98)
    fairness_audit_status = Column(String, default="VERIFIED_ETHICAL")
    audit_trail_hash = Column(String, nullable=False)

    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
