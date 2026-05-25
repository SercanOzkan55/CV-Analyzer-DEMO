# API Examples

Run the backend demo first:

```bash
cd backend_demo
uvicorn main:app --reload --port 8001
```

## Analyze One CV

```bash
curl -X POST http://127.0.0.1:8001/api/v1/analyze ^
  -H "Content-Type: application/json" ^
  -d "{\"cv_text\":\"Python FastAPI SQL engineer\",\"job_description\":\"Backend role with Python and SQL\",\"required_skills\":[\"Python\",\"SQL\"]}"
```

## Rank Multiple Candidates

```json
{
  "job_description": "Backend engineer with Python, FastAPI, SQL, and API design.",
  "required_skills": ["Python", "FastAPI", "SQL"],
  "nice_to_have_skills": ["Docker", "React"],
  "candidates": [
    {
      "candidate_id": "candidate_001",
      "cv_text": "Python backend engineer with FastAPI and PostgreSQL experience."
    },
    {
      "candidate_id": "candidate_002",
      "cv_text": "Marketing specialist with content strategy experience."
    }
  ]
}
```

The production API includes authentication, organization scoping, storage handling, quotas, and audit logs. Those layers are intentionally omitted here.