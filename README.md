# AI Data Analyst Agent – Working Starter

A FastAPI-based starter project for CSV/Excel profiling, numeric summaries, optional OpenRouter-generated explanations, and Plotly histogram endpoints. Includes a simple HTML/CSS/JS dashboard. Agent modules are scaffolded; **LangGraph orchestration, full natural-language analytics, advanced charts, authentication, and production deployment are future milestones**. The current chat flow computes fixed statistics and asks an LLM to explain them, rather than executing arbitrary generated code.

## Run on Windows (PowerShell)

```powershell
cd AI-Data-Analyst-Agent
py -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000 for the dashboard or http://127.0.0.1:8000/docs for API documentation.

If PowerShell blocks activation, run `Set-ExecutionPolicy -Scope Process Bypass` in that PowerShell session, then activate again.

## Optional AI explanations

Add your own OpenRouter API key to `.env` as `OPENROUTER_API_KEY=...` and configure a model available to your account. Never commit `.env`.

## Endpoints

- `POST /api/upload` multipart file upload (CSV/XLSX, max 10 MB)
- `GET /api/analytics/{dataset_id}` summary statistics
- `GET /api/chart/{dataset_id}/{column}` Plotly chart JSON
- `POST /api/chat` JSON `{"dataset_id":"...", "question":"..."}`
- `GET /health` service health

## Tests

```powershell
pytest -q
```

## Notes

This starter is intended for local development and trusted test datasets. Uploads persist locally and are not user-isolated. Do not deploy publicly without authentication, file scanning, data retention policies, resource limits, and authorization. AI requests send computed summary information to your configured provider; avoid sensitive data unless approved.
