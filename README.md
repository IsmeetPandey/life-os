# Life OS 🧠

> Turn daily behavior into measurable, reviewable observations.

Life OS is a **local-first personal feedback system** for logging daily activities and reviewing patterns without pretending that correlation proves causation.

## Why it exists

Most productivity tools collect numbers but make interpretation difficult. Life OS keeps the model simple: record what happened, validate the input, store it locally, and make the observations easy to review.

## Current MVP

- Local SQLite storage
- Daily activity logging
- Today-at-a-glance totals
- Historical observation count
- Validation for recorded minutes

## Quick start

```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
uvicorn app:app --reload
```

Open `http://127.0.0.1:8000`.

## Engineering principles

- **Local-first:** personal data stays in the local application database.
- **Evidence over assumptions:** the app reports observations and correlations rather than claiming causation.
- **Small primitives first:** reliable logging and validation come before advanced analytics.

## Quality & maintenance

- Dependency updates are managed with Dependabot.
- CI performs a Python compilation/smoke check on pushes and pull requests.
- Contributions are documented in `CONTRIBUTING.md`.
- Security reports should follow `SECURITY.md`.

## Roadmap

- [ ] Trend charts
- [ ] Target tracking
- [ ] Uncertainty-aware comparisons
- [ ] Weekly review
- [ ] Exportable reports

## Scope

This is a personal analytics project, not a medical, financial, or professional decision-making system. Treat its output as observations about recorded data, not as authoritative conclusions.
