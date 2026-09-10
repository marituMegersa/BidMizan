from sqlalchemy.orm import Session
import uuid
import datetime
from app.domain.procurement_bidding.models import ProcurementBiddingRecord
from app.domain.procurement_bidding.schemas import ProcurementBiddingRequest

class ProcurementBiddingService:
    @staticmethod
    def process_encounter(db: Session, data: ProcurementBiddingRequest) -> ProcurementBiddingRecord:
        rec_id = f"REC-{uuid.uuid4().hex[:8]}"
        db_obj = ProcurementBiddingRecord(
            id=rec_id,
            created_at=datetime.datetime.utcnow()
        )
        return db_obj
