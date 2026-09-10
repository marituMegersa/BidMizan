import os

class Settings:
    PROJECT_NAME: str = "BidMizan Ethical Procurement & Tender AI API"
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://copilot_user:copilot_secure_password@localhost:5432/procurement_bidding_db")

settings = Settings()
