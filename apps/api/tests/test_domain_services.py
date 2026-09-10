def test_procurement_bidding_model_instantiation():
    from app.domain.procurement_bidding.models import ProcurementBiddingRecord
    rec = ProcurementBiddingRecord(id="REC-TEST-01")
    assert rec.id == "REC-TEST-01"

def test_procurement_bidding_schema_validation():
    from app.domain.procurement_bidding.schemas import ProcurementBiddingResponse
    res = ProcurementBiddingResponse(id="REC-TEST-01", status="COMPLETED", summary="Test", confidence_score=0.99, created_at="2026-09-10T16:00:00Z")
    assert res.status == "COMPLETED"
