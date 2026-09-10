from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.domain.procurement_bidding.router import router as domain_router

app = FastAPI(title="BidMizan API", description="Python FastAPI Backend for BidMizan", version="1.0.0")

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
    return {"status": "healthy", "service": "BidMizan"}
