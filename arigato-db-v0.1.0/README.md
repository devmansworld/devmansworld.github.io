# ARIGATO Database Bridge v0.1.0

Isolated backend experiment. This folder does not replace or modify the current ARIGATO Pages release.

## Architecture decision

- GitHub Pages remains the static frontend and release catalogue.
- A separately hosted FastAPI service provides the remote API.
- PostgreSQL is the production database. SQLite is supported only for local development.
- The frontend will run in **parallel storage mode** during migration: existing localStorage remains intact while API data is read/written through an explicit adapter.
- No automatic merge or destructive migration is included in this release.

## Why PostgreSQL for remote use?

A remote multi-device service needs a database server with managed persistence and backups. SQLite remains useful for local development, but a SQLite file on an ephemeral web host is not a reliable shared production database.

## First-release scope

- Health check
- Token-protected payment history
- Token-protected payment creation
- Cashflow totals grouped by month and currency
- CLP and USD remain separate; no currency conversion
- Amounts are integer minor units (CLP pesos / USD cents) to avoid floating-point errors

Appointments and people are represented in the initial data model, but their CRUD endpoints and legacy-data migration are deliberately deferred.

## Run locally

1. Copy `.env.example` to `.env` and set a long random `ARIGATO_API_TOKEN`.
2. Install dependencies: `python -m pip install -e .`
3. Start: `uvicorn app.main:app --reload`
4. Open `http://127.0.0.1:8000/docs`.

Without `DATABASE_URL`, development defaults to `sqlite:///./arigato.db`. For remote deployment, set a PostgreSQL URL and a persistent database.

## Remote deployment requirements

- Deploy this API separately from GitHub Pages.
- Set `DATABASE_URL`, `ARIGATO_API_TOKEN`, and `CORS_ORIGINS` as host secrets/environment variables.
- Use a managed PostgreSQL database with automated backups.
- Require HTTPS at the hosting edge.
- Never commit `.env`, tokens, database files, or customer data.
- Restrict CORS to the exact published frontend origins. CORS is not authentication.
- Rotate the API token if it is exposed. A single shared token is an initial single-owner bridge, not a multi-user identity system.

## Parallel migration policy

The existing browser store remains authoritative until explicit reconciliation is complete. API writes must be opt-in in the frontend. Do not dual-write automatically: partial failures can create divergent records. Each imported record will need a stable source ID and an idempotent migration process before cutover.

## Version

- Version: 0.1.0
- Status: isolated backend foundation; not deployed
- Changelog: initial scaffold
