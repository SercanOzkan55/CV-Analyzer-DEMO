# Architecture Overview

The private CV Analyzer system is organized as a modular SaaS platform. This public demo only keeps a small representative slice.

## Private Production Architecture

```mermaid
flowchart LR
  Web["React / Vite Web App"] --> API["FastAPI API Gateway"]
  Worker["Local Desktop Worker"] --> API
  API --> Auth["Auth / Tenant Guards"]
  API --> Quota["Quota + Billing"]
  API --> Pipeline["CV Processing Pipeline"]
  Pipeline --> Extract["PDF / DOCX Extraction"]
  Pipeline --> Rules["Deterministic ATS Rules"]
  Pipeline --> ML["ML Calibration"]
  Pipeline --> AI["Optional AI Review"]
  API --> DB["PostgreSQL"]
  API --> Storage["Private Object Storage"]
```

## Public Demo Architecture

```mermaid
flowchart LR
  DemoUI["frontend_demo"] --> DemoAPI["backend_demo FastAPI"]
  DemoWorker["local_worker_demo"] --> DemoScoring["scoring.py"]
  DemoAPI --> DemoScoring
```

## Important Production Features Not Published

- tenant-scoped recruiter workspaces
- secure worker key lifecycle
- row-level quota accounting
- audit logging and secret redaction
- storage signed URL isolation
- production ML feature extraction
- OpenAI/provider fallback controls
- full frontend dashboard and local worker desktop UI

The public demo focuses on product direction and simplified scoring mechanics only.