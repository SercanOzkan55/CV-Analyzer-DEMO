# CV Analyzer DEMO

This repository is a **public, intentionally trimmed demo** of a much larger private SaaS project.

The full CV Analyzer product is a private codebase of roughly **160,000 lines of code** across:

- FastAPI backend services
- React/Vite web dashboard
- recruiter and candidate workflows
- ATS and ML-assisted scoring pipelines
- local desktop worker architecture
- quota, billing, storage, audit, and security layers

This public repository is shared only to communicate the architecture, engineering direction, and product thinking behind the project. It is **not** the full production system.

## Why This Repo Is Trimmed

The production repository contains private implementation details, security-sensitive flows, business logic, model calibration code, deployment configuration, and user-data handling logic. Those parts are intentionally not published.

Omitted from this demo:

- production authentication and tenant isolation code
- Stripe billing and quota enforcement internals
- full SQLAlchemy model graph and Alembic migrations
- real object storage integration
- real CV datasets and parsed candidate data
- trained model files and calibration pipeline internals
- OpenAI/provider integration details
- full recruiter dashboard UI
- packaged desktop worker build artifacts
- secrets, environment files, logs, database files, and private test data

## What Is Included

This demo keeps enough working code to show the core idea:

- a small FastAPI backend demo
- deterministic CV/job matching logic
- Pydantic request/response models
- a minimal React UI concept
- a simplified local worker CLI concept
- architecture and privacy documentation
- sample CV and job description text
- a small unit test suite for the scoring logic

## Repository Map

```text
backend_demo/
  main.py            # FastAPI demo endpoints
  schemas.py         # public-safe Pydantic contracts
  scoring.py         # simplified deterministic scoring logic
  requirements.txt
  tests/

frontend_demo/
  src/App.jsx        # compact product UI mock
  src/styles.css

local_worker_demo/
  worker.py          # simplified offline folder scoring concept

docs/
  ARCHITECTURE.md
  API_EXAMPLES.md
  PRIVACY_AND_SCOPE.md

sample_data/
  sample_cv.txt
  sample_job.txt
```

## Quick Start: Backend Demo

```bash
cd backend_demo
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8001
```

Open:

```text
http://127.0.0.1:8001/docs
```

Example request:

```bash
curl -X POST http://127.0.0.1:8001/api/v1/analyze ^
  -H "Content-Type: application/json" ^
  -d "{\"cv_text\":\"Python FastAPI React SQL experience\",\"job_description\":\"Backend engineer with Python FastAPI SQL\",\"required_skills\":[\"Python\",\"FastAPI\",\"SQL\"]}"
```

## Quick Start: Frontend Demo

```bash
cd frontend_demo
npm install
npm run dev
```

The frontend is intentionally a visual/product demo, not the full private dashboard.

## Quick Start: Local Worker Concept

```bash
cd local_worker_demo
python worker.py --cv-folder ../sample_data --job-file ../sample_data/sample_job.txt
```

The production local worker is a private desktop application with offline-first processing, queueing, sync, and quota-safe claim/result semantics. This demo only shows the local-folder scoring idea.

## Engineering Themes Demonstrated

- deterministic scoring before AI calls, to control cost
- explainable matching output for recruiters
- privacy-first local processing model
- API contracts designed for product integration
- separation between demo logic and production-sensitive systems

## Important Note

This repository is a **portfolio/demo artifact**. It is not intended to be deployed as a production hiring system.

For a technical review, I can walk through the private system architecture, production tradeoffs, and omitted modules at a high level without exposing sensitive code or user data.