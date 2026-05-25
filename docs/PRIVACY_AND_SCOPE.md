# Privacy and Scope

This public demo is intentionally designed to avoid exposing private production logic or user data.

## No Private Data

This repo does not include:

- real CVs
- recruiter notes
- parsed candidate records
- production databases
- object storage keys
- provider API keys
- private logs
- trained private model artifacts

## Demo-Only Logic

The included scoring logic is simplified and deterministic. The private product has a richer parsing, normalization, ATS scoring, ML calibration, and optional AI review pipeline.

## Local Processing Direction

The private product includes a local worker concept for privacy-sensitive recruiter workflows. The worker can process large local CV folders and sync selected results back to the SaaS account. This public repo includes only a minimal CLI concept to explain that direction.

## Security Posture

Production security details are intentionally abstracted in this demo. At a high level, the private system is designed around:

- tenant isolation
- short-lived worker sessions
- no plaintext API key storage
- signed storage URLs
- quota-safe claim/result transactions
- audit events
- secret redaction