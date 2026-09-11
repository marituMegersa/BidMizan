from pydantic import BaseModel, Field
from typing import List, Optional
from app.schemas.domain import TenderAuditResponse

class TenderSearchQuery(BaseModel):
    min_fairness: Optional[float] = Field(None, example=80.0)
    status: Optional[str] = Field(None, example="PASSED_ETHICAL_AUDIT")
    page: int = Field(1, ge=1)
    page_size: int = Field(20, ge=1, le=100)

class PaginatedTenderResponse(BaseModel):
    items: List[TenderAuditResponse]
    total: int
    page: int
    page_size: int
    total_pages: int

# Search & Pagination Criteria Filter
