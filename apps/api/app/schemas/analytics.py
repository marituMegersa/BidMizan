from pydantic import BaseModel, Field
from typing import Dict, List

class ProcurementAnalyticsResponse(BaseModel):
    total_tenders_audited: int = Field(..., example=650)
    passed_ethical_audits: int = Field(..., example=590)
    flagged_collusion_tenders: int = Field(..., example=60)
    average_fairness_score: float = Field(..., example=91.8)
    sha256_verification_pass_rate_pct: float = Field(..., example=100.0)
