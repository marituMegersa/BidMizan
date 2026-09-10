from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from datetime import datetime

class ProcurementBiddingRequest(BaseModel):

    tender_id: str
    vendor_name: str
    bid_amount: float
    technical_proposal_summary: str


class ProcurementBiddingResponse(BaseModel):
    id: str
    status: str = "COMPLETED"
    summary: str
    confidence_score: float = 0.98
    created_at: datetime

    class Config:
        from_attributes = True
