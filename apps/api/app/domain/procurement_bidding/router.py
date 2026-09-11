from fastapi import APIRouter
from app.domain.procurement_bidding.schemas import TenderAuditRequest, TenderAuditResponse
from app.domain.procurement_bidding.service import ProcurementBiddingService

router = APIRouter(prefix="/api/v1/procurement_bidding", tags=["Procurement Fraud Detection & Audit"])

@router.post("/audit", response_model=TenderAuditResponse)
def audit_tender(req: TenderAuditRequest):
    return ProcurementBiddingService.audit_tender(req)
