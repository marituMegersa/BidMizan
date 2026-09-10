# BidMizan — Ethical Procurement & Tender AI ⚖️🏛️

[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black)](https://react.dev/)
[![Ethics](https://img.shields.io/badge/Ethics-Tamper--Proof%20Audit-emerald?style=for-the-badge)]()

**Ethical Procurement Fraud Detection, Bid Anomaly Auditor & Fairness Evaluation Engine**

---

## 🌟 Key Features

- **Automated Fraud & Anomaly Detector**: Scans tender bids for price collusion, abnormal price swings, and vendor conflicts.
- **Compliance Audit Score Engine**: Evaluates vendor technical proposals against statutory procurement regulations.
- **SHA-256 Tamper-Proof Audit Trail**: Cryptographically hashes bid submission logs for immutable auditability.
- **Fair Procurement Dashboard**: Visualizes vendor compliance metrics, pricing distribution, and audit results.

---

## 📂 Monorepo Structure

```text
BidMizan/
├── apps/
│   ├── api/                     # Python 3.12 FastAPI Backend
│   │   ├── app/domain/procurement_bidding/
│   │   │   ├── models.py        # Tender & Vendor Bid ORM Models
│   │   │   ├── schemas.py       # Pydantic v2 Procurement Schemas
│   │   │   ├── service.py       # Fraud Detection & Audit Engine
│   │   │   └── router.py        # REST Endpoints
│   │   └── main.py
│   └── web/                     # React 18 Procurement Dashboard
├── docker-compose.yml
└── README.md
```

---

## 🚀 Quick Start
```bash
# Backend
cd apps/api && pip install -r requirements.txt && python main.py

# Frontend
cd apps/web && npm install && npm run dev
```
