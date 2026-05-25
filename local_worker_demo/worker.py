from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "backend_demo"))

from scoring import score_cv  # noqa: E402


def read_text_files(folder: Path) -> list[Path]:
    return sorted(path for path in folder.glob("*.txt") if path.is_file())


def main() -> int:
    parser = argparse.ArgumentParser(description="CV Analyzer public local worker demo")
    parser.add_argument("--cv-folder", required=True, help="Folder with .txt CV files")
    parser.add_argument("--job-file", required=True, help="Text file containing the job description")
    parser.add_argument("--output", default="local_worker_demo_results.json")
    args = parser.parse_args()

    cv_folder = Path(args.cv_folder)
    job_text = Path(args.job_file).read_text(encoding="utf-8")

    rows = []
    for cv_file in read_text_files(cv_folder):
        if cv_file.name == Path(args.job_file).name:
            continue
        result = score_cv(
            cv_text=cv_file.read_text(encoding="utf-8"),
            job_description=job_text,
            required_skills=["Python", "FastAPI", "SQL"],
            nice_to_have_skills=["React", "Docker"],
        )
        rows.append(
            {
                "file": cv_file.name,
                "score": result.score,
                "decision": result.decision,
                "explanation": result.explanation,
            }
        )

    rows.sort(key=lambda row: row["score"], reverse=True)
    Path(args.output).write_text(json.dumps(rows, indent=2), encoding="utf-8")
    print(f"Wrote {len(rows)} result(s) to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())