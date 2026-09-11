# BidMizan Ethical Procurement AI

[![FastAPI](https://img.shields.io/badge/FastAPI-0.110.0-009688.svg?style=flat&logo=fastapi)](https://fastapi.tiangolo.com)
[![React](https://img.shields.io/badge/React-18-61DAFB.svg?style=flat&logo=react)](https://react.dev)
[![Python](https://img.shields.io/badge/Python-3.12-3776AB.svg?style=flat&logo=python)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

> **Procurement Collusion Detection & Cryptographic Tender Audit Platform**

An AI platform for transparent public procurement. Analyzes bid pricing distributions for price-fixing collusion, computes variance-coefficient fairness scores, and records cryptographic SHA-256 audit hashes for tamper-proof compliance.

---

## 🏛️ Clean Architecture Overview

This repository is built following **Clean Layered Architecture** standards:

```
apps/api/app/
├── api/          # Thin REST routers & Dependency Injection (deps.py)
├── schemas/      # Pydantic v2 validation DTOs (Request / Response)
├── models/       # SQLAlchemy 2.0 Async ORM models & Base declarative metadata
├── repositories/ # Dedicated async database access queries ONLY
├── services/     # Pure business logic, domain rules, & AI orchestrators
├── core/         # Settings (pydantic-settings), Async Database, JWT Security, & Exceptions
└── utils/        # Reusable helper utilities
```

---

## ✨ Key Features

- **Collusion Detection**:  Coefficient of Variation (CV) analysis to flag bidder rings
- **Cryptographic Audit**:  SHA-256 hash generation for verifiable bid history
- **Audit Ledger**:  Async database storage of audited tenders and fairness scores
- **Procurement Dashboard**:  React 18 UI displaying risk meters and tender audit trails

---

## 🛠️ Tech Stack

- **Backend**: Python 3.12, FastAPI 0.110+, Async SQLAlchemy 2.0+, Pydantic v2
- **Frontend**: React 18, TypeScript, Tailwind CSS, Lucide Icons
- **Database & Cache**: PostgreSQL (Asyncpg), Redis, Elasticsearch
- **AI & RAG**: vLLM / Ollama, LangChain, LangGraph State Graphs
- **DevOps & Testing**: Docker, Docker Compose, Pytest, Pytest-Asyncio

---

## 🚀 Quick Start Guide

### 1. Prerequisites
- Docker & Docker Compose
- Python 3.12+
- Node.js 20+

### 2. Backend Setup
```bash
# Navigate to API directory
cd apps/api

# Install dependencies
pip install -r requirements.txt

# Run database migrations & start FastAPI app
python main.py
# API running at http://localhost:8000 (Swagger docs at http://localhost:8000/docs)
```

### 3. Frontend Setup
```bash
# Navigate to Web app directory
cd apps/web

# Install dependencies & start dev server
npm install
npm run dev
# Web app running at http://localhost:3000
```

### 4. Running via Docker Compose
```bash
docker-compose up --build
```

---

## 🧪 Testing

Run unit & integration tests using `pytest`:
```bash
cd apps/api
pytest tests/ -v
```

---

## 📜 API Documentation

Once started, interactive API documentation is available at:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

**Primary Endpoint Sample**:
`POST /api/v1/procurement/audit`

---

## 👤 Author & Maintainer

Maintained with ❤️ by **[marituMegersa](https://github.com/marituMegersa)**.
