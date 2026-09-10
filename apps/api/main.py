from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.domain.procurement_bidding.router import router as domain_router

app = FastAPI(title="BidMizan Ethical Procurement & Tender AI API", description="Ethical Procurement Fraud Detection, Bid Auditor & Fairness Score Engine", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(domain_router)

@app.get("/health")
def health():
    return {"status": "healthy", "service": "BidMizan Ethical Procurement & Tender AI"}
