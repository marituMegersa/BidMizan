from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.deps import get_db
from app.repositories.domain import ProcurementBiddingRepository
from app.schemas.analytics import ProcurementAnalyticsResponse
from app.services.analytics import ProcurementAnalyticsService

router = APIRouter(prefix="/analytics", tags=["Procurement Fraud Analytics"])

@router.get("", response_model=ProcurementAnalyticsResponse)
async def get_analytics(db: AsyncSession = Depends(get_db)):
    repo = ProcurementBiddingRepository(db)
    service = ProcurementAnalyticsService(repo)
    return await service.get_procurement_analytics()
