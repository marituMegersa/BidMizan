from sqlalchemy import Column, String, DateTime
import datetime
from app.db.base import Base

class ProcurementAuditor(Base):
    __tablename__ = "procurement_auditors"

    id = Column(String, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    badge_number = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
