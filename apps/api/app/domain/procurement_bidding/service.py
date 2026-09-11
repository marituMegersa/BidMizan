from sqlalchemy.orm import Session
from typing import List
import uuid
from app.domain.procurement_bidding.models import ProcurementBiddingRecord
from app.domain.procurement_bidding.schemas import TenderAuditRequest, TenderAuditResponse
from app.domain.procurement_bidding.engine import ProcurementFraudEngine

class ProcurementBiddingService:
    @staticmethod
    def audit_and_store(db: Session, req: TenderAuditRequest) -> TenderAuditResponse:
        res = ProcurementFraudEngine.audit_tender_bids(req.tender_id, req.bid_prices)
        
        record_id = f"BID-{uuid.uuid4().hex[:8].upper()}"
        db_obj = ProcurementBiddingRecord(
            id=record_id,
            tender_id=req.tender_id,
            fairness_score=res["fairness_score"],
            audit_status=res["status"],
            sha256_hash=res["sha256_hash"]
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        
        return TenderAuditResponse(
            tender_id=db_obj.tender_id,
            fairness_score=db_obj.fairness_score,
            audit_status=db_obj.audit_status,
            sha256_hash=db_obj.sha256_hash,
            recommendations=res["recommendations"],
            audited_at=db_obj.created_at
        )

    @staticmethod
    def list_audits(db: Session, skip: int = 0, limit: int = 50) -> List[ProcurementBiddingRecord]:
        return db.query(ProcurementBiddingRecord).offset(skip).limit(limit).all()
