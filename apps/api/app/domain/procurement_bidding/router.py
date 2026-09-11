from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_async_db
from app.domain.procurement_bidding.service import ProcurementAuditLangGraphService

router = APIRouter(prefix="/api/v1/procurement_bidding", tags=["BidMizan — Ethical Procurement & Tender AI"])

@router.get("/healthz")
async def async_health_check():
    return {"status": "healthy", "architecture": "Async SQLAlchemy + LangGraph + Redis + Elasticsearch"}

@router.post("/agentic-eval")
async def run_agentic_eval(payload: dict, db: AsyncSession = Depends(get_async_db)):
    return await ProcurementAuditLangGraphService.evaluate_async(db, payload)
