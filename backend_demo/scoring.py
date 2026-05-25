from __future__ import annotations

import re
from dataclasses import dataclass


WORD_RE = re.compile(r"[a-zA-Z0-9+#.\-]{2,}")


@dataclass(frozen=True)
class ScoreResult:
    score: float
    decision: str
    confidence: str
    matched_skills: list[str]
    missing_skills: list[str]
    risk_flags: list[str]
    explanation: str
    breakdown: dict[str, float]


def normalize_tokens(text: str) -> set[str]:
    return {token.lower().strip(".,;:()[]{}") for token in WORD_RE.findall(text)}


def phrase_present(text: str, phrase: str) -> bool:
    if not phrase.strip():
        return False
    pattern = re.escape(phrase.strip().lower())
    return bool(re.search(rf"(?<!\w){pattern}(?!\w)", text.lower()))


def coverage_score(text: str, skills: list[str]) -> tuple[float, list[str], list[str]]:
    if not skills:
        return 100.0, [], []

    matched: list[str] = []
    missing: list[str] = []
    for skill in skills:
        if phrase_present(text, skill):
            matched.append(skill)
        else:
            missing.append(skill)

    return round((len(matched) / len(skills)) * 100, 2), matched, missing


def keyword_overlap_score(cv_text: str, job_description: str) -> float:
    cv_tokens = normalize_tokens(cv_text)
    job_tokens = normalize_tokens(job_description)
    if not job_tokens:
        return 0.0

    overlap = cv_tokens & job_tokens
    return round((len(overlap) / len(job_tokens)) * 100, 2)


def decide(score: float, risk_flags: list[str]) -> tuple[str, str]:
    if risk_flags and score < 80:
        return "recommended_reject", "medium"
    if score >= 75:
        return "recommended_accept", "high"
    if score >= 50:
        return "recommended_review", "medium"
    return "recommended_reject", "low"


def score_cv(
    cv_text: str,
    job_description: str,
    required_skills: list[str] | None = None,
    nice_to_have_skills: list[str] | None = None,
    hard_reject_criteria: list[str] | None = None,
) -> ScoreResult:
    required_skills = required_skills or []
    nice_to_have_skills = nice_to_have_skills or []
    hard_reject_criteria = hard_reject_criteria or []

    keyword_score = keyword_overlap_score(cv_text, job_description)
    required_score, required_matched, missing_required = coverage_score(cv_text, required_skills)
    nice_score, nice_matched, _ = coverage_score(cv_text, nice_to_have_skills)

    risk_flags = [
        criterion
        for criterion in hard_reject_criteria
        if phrase_present(cv_text, criterion)
    ]
    hard_reject_penalty = min(30.0, len(risk_flags) * 15.0)

    final = (
        keyword_score * 0.30
        + required_score * 0.45
        + nice_score * 0.15
        + 10.0
        - hard_reject_penalty
    )
    final_score = round(max(0.0, min(100.0, final)), 2)
    decision, confidence = decide(final_score, risk_flags)

    matched = required_matched + nice_matched
    explanation = (
        f"Matched {len(matched)} skill(s), missing {len(missing_required)} required skill(s), "
        f"keyword overlap {keyword_score}%."
    )

    return ScoreResult(
        score=final_score,
        decision=decision,
        confidence=confidence,
        matched_skills=matched,
        missing_skills=missing_required,
        risk_flags=risk_flags,
        explanation=explanation,
        breakdown={
            "keyword_score": keyword_score,
            "required_skill_score": required_score,
            "nice_to_have_score": nice_score,
            "hard_reject_penalty": hard_reject_penalty,
            "final_score": final_score,
        },
    )