from pydantic import BaseModel, Field
from typing import List
from datetime import datetime

class TenderAuditRequest(BaseModel):
    tender_id: str = Field(..., example="TENDER-ETH-2026-88")
    bid_prices: List[float] = Field(..., example=[500000.0, 502000.0, 501500.0])

class TenderAuditResponse(BaseModel):
    tender_id: str
    fairness_score: float
    audit_status: str
    sha256_hash: str
    recommendations: List[str]
    audited_at: datetime = Field(default_factory=datetime.utcnow)
