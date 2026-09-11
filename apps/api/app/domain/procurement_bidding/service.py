from app.domain.procurement_bidding.engine import ProcurementFraudEngine
from app.domain.procurement_bidding.schemas import TenderAuditRequest, TenderAuditResponse

class ProcurementBiddingService:
    @staticmethod
    def audit_tender(req: TenderAuditRequest) -> TenderAuditResponse:
        res = ProcurementFraudEngine.audit_tender_bids(req.tender_id, req.bid_prices)
        return TenderAuditResponse(
            tender_id=req.tender_id,
            fairness_score=res["fairness_score"],
            audit_status=res["status"],
            sha256_hash=res["sha256_hash"],
            recommendations=res["recommendations"]
        )
