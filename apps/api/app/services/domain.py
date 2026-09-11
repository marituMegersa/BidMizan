from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
import uuid
import hashlib
import datetime

from app.models.domain import ProcurementBiddingRecord
from app.repositories.domain import ProcurementBiddingRepository
from app.schemas.domain import TenderAuditRequest, TenderAuditResponse

class ProcurementBiddingService:
    def __init__(self, repo: ProcurementBiddingRepository):
        self.repo = repo

    async def audit_tender_bids(self, req: TenderAuditRequest) -> TenderAuditResponse:
        prices = req.bid_prices
        avg_price = sum(prices) / len(prices) if prices else 0.0
        variance = sum((p - avg_price) ** 2 for p in prices) / max(len(prices), 1)
        cv = (variance ** 0.5) / max(avg_price, 1.0)

        is_suspicious = cv < 0.05
        fairness = 45.0 if is_suspicious else 95.0
        status_str = "FLAGGED_PRICE_COLLUSION" if is_suspicious else "PASSED_ETHICAL_AUDIT"
        sha_hash = hashlib.sha256(f"{req.tender_id}:{prices}".encode()).hexdigest()

        record_id = f"BID-{uuid.uuid4().hex[:8].upper()}"
        db_obj = ProcurementBiddingRecord(
            id=record_id,
            tender_id=req.tender_id,
            fairness_score=fairness,
            audit_status=status_str,
            sha256_hash=sha_hash,
            created_at=datetime.datetime.utcnow()
        )
        saved = await self.repo.create(db_obj)

        return TenderAuditResponse(
            tender_id=saved.tender_id,
            fairness_score=saved.fairness_score,
            audit_status=saved.audit_status,
            sha256_hash=saved.sha256_hash,
            recommendations=["Mandatory collusion investigation triggered." if is_suspicious else "Procurement fairness satisfied."],
            audited_at=saved.created_at or datetime.datetime.utcnow()
        )

    async def list_audit_logs(self, skip: int = 0, limit: int = 50) -> List[ProcurementBiddingRecord]:
        return await self.repo.get_multi(skip=skip, limit=limit)

# Business logic & AI engine orchestrator
