import React from "react";
import { createRoot } from "react-dom/client";
import "./styles.css";

const metrics = [
  ["Candidates", "342", "Ready to analyze"],
  ["Avg. Match", "78%", "Across all candidates"],
  ["Shortlisted", "128", "Above review threshold"],
  ["Hard Rejects", "42", "Filtered out"],
];

const rows = [
  ["A-1042", "Senior Backend Engineer", "91", "recommended_accept"],
  ["A-1017", "Full Stack Developer", "76", "recommended_review"],
  ["A-0988", "Junior Developer", "48", "recommended_reject"],
];

function App() {
  return (
    <main className="app">
      <aside className="sidebar">
        <div className="brand">
          <div className="logo">CV</div>
          <div>
            <strong>CV Analyzer</strong>
            <span>Public demo</span>
          </div>
        </div>
        <nav>
          <a className="active">Analyze</a>
          <a>Recruiter</a>
          <a>Dashboard</a>
          <a>Local Worker</a>
          <a>Reports</a>
        </nav>
      </aside>

      <section className="content">
        <header>
          <div>
            <p className="eyebrow">Resume Intelligence</p>
            <h1>Explainable CV ranking for recruiter workflows</h1>
            <p className="lede">
              This public UI is a small representation of the private SaaS product.
              The production system contains the full dashboard, tenant isolation,
              local worker sync, quota controls, and model calibration layers.
            </p>
          </div>
          <button>Run sample analysis</button>
        </header>

        <section className="metrics">
          {metrics.map(([label, value, note]) => (
            <article key={label}>
              <span>{label}</span>
              <strong>{value}</strong>
              <small>{note}</small>
            </article>
          ))}
        </section>

        <section className="grid">
          <article className="panel">
            <h2>Scoring criteria</h2>
            <div className="chips">
              <span>Python</span>
              <span>FastAPI</span>
              <span>SQL</span>
              <span>React</span>
              <span>Leadership</span>
            </div>
            <textarea defaultValue="Backend engineer role with Python, FastAPI, PostgreSQL, API design, and production ownership." />
          </article>

          <article className="panel">
            <h2>Candidate ranking</h2>
            <table>
              <thead>
                <tr>
                  <th>ID</th>
                  <th>Role fit</th>
                  <th>Score</th>
                  <th>Decision</th>
                </tr>
              </thead>
              <tbody>
                {rows.map((row) => (
                  <tr key={row[0]}>
                    {row.map((cell) => <td key={cell}>{cell}</td>)}
                  </tr>
                ))}
              </tbody>
            </table>
          </article>
        </section>
      </section>
    </main>
  );
}

createRoot(document.getElementById("root")).render(<App />);