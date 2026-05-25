from __future__ import annotations

from pydantic import BaseModel, Field


class AnalyzeRequest(BaseModel):
    cv_text: str = Field(min_length=10, max_length=50_000)
    job_description: str = Field(min_length=10, max_length=50_000)
    required_skills: list[str] = Field(default_factory=list)
    nice_to_have_skills: list[str] = Field(default_factory=list)
    hard_reject_criteria: list[str] = Field(default_factory=list)


class ScoreBreakdown(BaseModel):
    keyword_score: float
    required_skill_score: float
    nice_to_have_score: float
    hard_reject_penalty: float
    final_score: float


class AnalyzeResponse(BaseModel):
    score: float
    decision: str
    confidence: str
    matched_skills: list[str]
    missing_skills: list[str]
    risk_flags: list[str]
    explanation: str
    breakdown: ScoreBreakdown


class BatchCandidate(BaseModel):
    candidate_id: str
    cv_text: str = Field(min_length=10, max_length=50_000)


class BatchRankRequest(BaseModel):
    job_description: str = Field(min_length=10, max_length=50_000)
    required_skills: list[str] = Field(default_factory=list)
    nice_to_have_skills: list[str] = Field(default_factory=list)
    hard_reject_criteria: list[str] = Field(default_factory=list)
    candidates: list[BatchCandidate]