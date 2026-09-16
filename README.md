# Life OS 🧠

A personal feedback system for turning daily behavior into measurable, reviewable insights.

## Product thesis

Most habit trackers record checkboxes. Life OS is designed to answer a harder question: **which behaviors correlate with better personal outcomes?**

## Planned system

```text
Daily inputs → validated data → trends → correlations → weekly review
```

### Core metrics

- Goals and measurable targets
- Study/work sessions
- Sleep duration and consistency
- Exercise / activity
- Distraction or screen-time data
- Daily outcome metrics

### Design principles

1. Observations are presented as correlations, not medical or scientific causation.
2. The product favors useful signals over notification spam.
3. Every metric must earn its place in the interface.

## Build phases

- **Phase 1:** local-first data model + daily logging
- **Phase 2:** trend dashboard + streak-free consistency metrics
- **Phase 3:** correlation explorer with uncertainty-aware language
- **Phase 4:** weekly review and export

## Intended stack

React + FastAPI + SQLite + a charting library.
