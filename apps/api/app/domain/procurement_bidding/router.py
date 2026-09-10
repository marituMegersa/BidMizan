from fastapi import APIRouter
from app.domain.procurement_bidding.service import *

router = APIRouter(prefix="/api/v1/procurement_bidding", tags=["BidMizan Ethical Procurement & Tender AI"])

@router.get("/status")
def get_domain_status():
    return {"status": "active", "domain": "BidMizan Ethical Procurement & Tender AI"}
