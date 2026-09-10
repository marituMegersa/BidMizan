from fastapi import APIRouter, status
from pydantic import BaseModel
from app.domain.procurement_bidding.service import ProcurementBiddingService

router = APIRouter(prefix="/api/v1/procurement_bidding", tags=["Procurement Bidding"])

class BidInput(BaseModel):
    tender_id: str
    vendor_name: str
    bid_amount: float
    technical_proposal_summary: str

@router.post("/audit_bid", status_code=status.HTTP_200_OK)
def audit_bid(data: BidInput):
    return ProcurementBiddingService.audit_bid(data.tender_id, data.vendor_name, data.bid_amount, data.technical_proposal_summary)
