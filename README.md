# Life OS 🧠

A local-first personal feedback system for turning daily behavior into measurable, reviewable observations.

## Run locally

```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
uvicorn app:app --reload
```

Open `http://127.0.0.1:8000`.

## Current MVP

- Local SQLite storage
- Daily activity logging
- Today-at-a-glance totals
- Observation count for historical data
- Input validation on recorded minutes

## Design principle

Life OS reports observations and correlations carefully. It does not pretend that a pattern in personal data proves causation.

Future versions: trend charts, target tracking, uncertainty-aware comparisons, weekly review, and export.
