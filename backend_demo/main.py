from __future__ import annotations

from fastapi import FastAPI

from schemas import AnalyzeRequest, AnalyzeResponse, BatchRankRequest
from scoring import score_cv


app = FastAPI(
    title="CV Analyzer DEMO API",
    version="0.1.0",
    description=(
        "Public demo API. The private production system includes additional "
        "auth, billing, storage, ML calibration, local worker sync, and audit layers."
    ),
)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "mode": "public-demo"}


@app.post("/api/v1/analyze", response_model=AnalyzeResponse)
def analyze(payload: AnalyzeRequest) -> AnalyzeResponse:
    result = score_cv(
        cv_text=payload.cv_text,
        job_description=payload.job_description,
        required_skills=payload.required_skills,
        nice_to_have_skills=payload.nice_to_have_skills,
        hard_reject_criteria=payload.hard_reject_criteria,
    )
    return AnalyzeResponse(**result.__dict__)


@app.post("/api/v1/recruiter/rank")
def rank_candidates(payload: BatchRankRequest) -> dict[str, list[dict]]:
    rows: list[dict] = []
    for candidate in payload.candidates:
        result = score_cv(
            cv_text=candidate.cv_text,
            job_description=payload.job_description,
            required_skills=payload.required_skills,
            nice_to_have_skills=payload.nice_to_have_skills,
            hard_reject_criteria=payload.hard_reject_criteria,
        )
        rows.append(
            {
                "candidate_id": candidate.candidate_id,
                "score": result.score,
                "decision": result.decision,
                "confidence": result.confidence,
                "matched_skills": result.matched_skills,
                "missing_skills": result.missing_skills,
                "risk_flags": result.risk_flags,
                "explanation": result.explanation,
            }
        )

    rows.sort(key=lambda row: row["score"], reverse=True)
    return {"results": rows}