from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional
from app.api.deps import get_db
from app.repositories.domain import ProcurementBiddingRepository
from app.schemas.search import PaginatedTenderResponse, TenderAuditResponse

router = APIRouter(prefix="/search", tags=["Search & Filter"])

@router.get("", response_model=PaginatedTenderResponse)
async def search_tenders(
    min_fairness: Optional[float] = Query(None),
    status: Optional[str] = Query(None),
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db)
):
    repo = ProcurementBiddingRepository(db)
    all_recs = await repo.get_multi(skip=(page - 1) * page_size, limit=page_size)
    items = [
        TenderAuditResponse(
            tender_id=r.tender_id,
            fairness_score=r.fairness_score,
            audit_status=r.audit_status,
            sha256_hash=r.sha256_hash,
            recommendations=["Verified procurement fairness."],
            audited_at=r.created_at
        ) for r in all_recs
    ]
    return PaginatedTenderResponse(
        items=items,
        total=len(items),
        page=page,
        page_size=page_size,
        total_pages=1
    )
