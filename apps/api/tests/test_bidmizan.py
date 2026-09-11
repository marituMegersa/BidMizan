import pytest
from app.services.domain import ProcurementBiddingService
from app.repositories.domain import ProcurementBiddingRepository
from app.schemas.domain import TenderAuditRequest

class MockSession:
    def add(self, obj): pass
    async def commit(self): pass
    async def refresh(self, obj): pass

@pytest.mark.asyncio
async def test_ethical_audit_passed():
    service = ProcurementBiddingService(ProcurementBiddingRepository(MockSession()))
    req = TenderAuditRequest(
        tender_id="TENDER-ETH-99",
        bid_prices=[450000.0, 520000.0, 480000.0, 600000.0]
    )
    res = await service.audit_tender_bids(req)
    assert res.audit_status == "PASSED_ETHICAL_AUDIT"
    assert res.fairness_score == 95.0
    assert len(res.sha256_hash) == 64

@pytest.mark.asyncio
async def test_collusion_flagged():
    service = ProcurementBiddingService(ProcurementBiddingRepository(MockSession()))
    req = TenderAuditRequest(
        tender_id="TENDER-ETH-100",
        bid_prices=[500000.0, 500100.0, 500050.0]
    )
    res = await service.audit_tender_bids(req)
    assert res.audit_status == "FLAGGED_PRICE_COLLUSION"
    assert res.fairness_score == 45.0
