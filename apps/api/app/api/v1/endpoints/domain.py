from fastapi import APIRouter, Depends, status, Query
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.api.deps import get_db
from app.schemas.domain import TenderAuditRequest, TenderAuditResponse
from app.repositories.domain import ProcurementBiddingRepository
from app.services.domain import ProcurementBiddingService

router = APIRouter(prefix="/procurement", tags=["Procurement Fraud Detection"])

def get_service(db: AsyncSession = Depends(get_db)) -> ProcurementBiddingService:
    repo = ProcurementBiddingRepository(db)
    return ProcurementBiddingService(repo)

@router.post("/audit", response_model=TenderAuditResponse, status_code=status.HTTP_201_CREATED)
async def audit_tender(req: TenderAuditRequest, service: ProcurementBiddingService = Depends(get_service)):
    return await service.audit_tender_bids(req)

@router.get("/audit-log")
async def list_audit_logs(skip: int = Query(0, ge=0), limit: int = Query(50, le=100), service: ProcurementBiddingService = Depends(get_service)):
    return await service.list_audit_logs(skip=skip, limit=limit)
