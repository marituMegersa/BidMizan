from fastapi import APIRouter, Depends, status, Query
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.domain.procurement_bidding.schemas import TenderAuditRequest, TenderAuditResponse
from app.domain.procurement_bidding.service import ProcurementBiddingService

router = APIRouter(prefix="/api/v1/procurement_bidding", tags=["Procurement Fraud Detection"])

@router.post("/audit", response_model=TenderAuditResponse, status_code=status.HTTP_201_CREATED)
def audit_tender(req: TenderAuditRequest, db: Session = Depends(get_db)):
    return ProcurementBiddingService.audit_and_store(db, req)

@router.get("/audit-log")
def list_audit_logs(skip: int = Query(0, ge=0), limit: int = Query(50, le=100), db: Session = Depends(get_db)):
    return ProcurementBiddingService.list_audits(db, skip=skip, limit=limit)
