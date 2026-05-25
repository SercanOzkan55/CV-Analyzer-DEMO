from scoring import score_cv


def test_high_match_candidate_is_recommended():
    result = score_cv(
        cv_text="Backend engineer with Python, FastAPI, PostgreSQL and React experience.",
        job_description="Hiring a backend engineer with Python, FastAPI and SQL.",
        required_skills=["Python", "FastAPI"],
        nice_to_have_skills=["React"],
    )

    assert result.score >= 75
    assert result.decision == "recommended_accept"
    assert "Python" in result.matched_skills


def test_missing_required_skill_lowers_score():
    result = score_cv(
        cv_text="Designer with Figma and branding experience.",
        job_description="Backend engineer with Python and FastAPI.",
        required_skills=["Python", "FastAPI"],
    )

    assert result.score < 75
    assert set(result.missing_skills) == {"Python", "FastAPI"}


def test_hard_reject_adds_risk_flag():
    result = score_cv(
        cv_text="Frontend developer with JavaScript but no professional experience.",
        job_description="Frontend developer role.",
        required_skills=["JavaScript"],
        hard_reject_criteria=["no professional experience"],
    )

    assert result.risk_flags == ["no professional experience"]
    assert result.breakdown["hard_reject_penalty"] > 0