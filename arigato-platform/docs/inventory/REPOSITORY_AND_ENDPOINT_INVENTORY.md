# ARIGATO Platform Migration — Repository & Endpoint Inventory

**Inventory date:** 2026-11-23  
**Repository:** `devmansworld/devmansworld.github.io`  
**Baseline branch:** `master`  
**Inventory branch:** `arigato-platform-foundation`  
**Baseline commit:** `bfd6a6543b2a44aaf7fa43fc703a4f6567cf47c8`  
**Status:** Discovery snapshot; no application code or production data changed.

## 1. Locked target architecture

| Concern | Decision |
|---|---|
| Backend | Spring Boot + Java 17 |
| Database | Existing ARIGATO database, remote access |
| Web client | Existing ARIGATO web application |
| Web automation | Playwright + TypeScript |
| Mobile client | React Native + TypeScript |
| Mobile UI automation | Appium Java Client directly |
| API automation | Karate + Java |
| Delivery | Remote hosting; parallel development |

Karate is assigned to API testing. Native mobile UI automation is assigned to the Appium Java Client. This avoids coupling mobile UI tests to Karate's legacy native driver integration.

## 2. Repository layout observed

The repository is a public GitHub Pages website, default branch `master`.

Relevant paths:

- `agenda/index.html` — published ARIGATO demo entry page.
- `agenda/current/index.html` — current working snapshot inspected for this inventory.
- `agenda/README.md` — product and privacy notes (its heading says v0.5.0).
- `agenda/services.json` — public read-only service catalogue.
- `agenda/mock-requestors.json` — synthetic demo requestors.
- `agenda/payment-lab-v0.1.0/index.html` — isolated payment-history/cash-flow experiment.
- `agenda/repair-v0.6.3/`, `agenda/repair-v0.6.4/`, `agenda/repair-v0.6.5/` — preserved repair snapshots.
- `stable/historic/agenda-one/`, `agenda-two/`, `agenda-three/` — historic iterations.
- `stable/versions/v0.6.0/` — version snapshot.
- `stable/` — launch/documentation landing area.

The inspected `agenda/current/index.html` identifies itself as ARIGATO v0.6.0. The README heading still identifies v0.5.0. Treat the code header and snapshot path as evidence of the current working copy, but reconcile release metadata before tagging a new product release.

## 3. Runtime behaviour and persistence

The current working copy is a static HTML/CSS/JavaScript application. It uses FullCalendar 6.1.15 from jsDelivr and browser `localStorage`. It explicitly describes itself as local-first, without login, backend, synchronization or remote storage.

Observed local storage keys:

| Key | Purpose |
|---|---|
| `agenda-demo-v0.3.0` | Appointment records |
| `agenda-requestors-v1` | People/requestor records |
| `arigato-payments-v1` | Payment records |
| `agenda-language` | UI language |
| `agenda-theme-index` | Theme selection |
| `agenda-requestor-term` | Preferred label for the person/requestor concept |

The application also migrates older appointment data from `agenda-demo-v0.1.0` when the current appointment collection is empty. Existing keys are not automatically deleted.

## 4. Endpoint inventory — existing live HTTP resources

**No dynamic REST API endpoints were found in the inspected ARIGATO application.** The only application-owned HTTP resources fetched by the current client are static JSON files hosted on GitHub Pages.

| Method | Existing URL | Purpose | Mutability |
|---|---|---|---|
| GET | `https://devmansworld.github.io/agenda/services.json` | Service catalogue | Static read-only |
| GET | `https://devmansworld.github.io/agenda/mock-requestors.json` | Synthetic demo people/requestors | Static read-only |

Third-party resources:

| Method | Resource | Purpose |
|---|---|---|
| GET | jsDelivr FullCalendar 6.1.15 CSS/JS | Calendar UI library and locale bundle |

There are no observed server-side create/update/delete endpoints for appointments, requestors or payments. Those records are persisted only in the browser.

## 5. Existing data contracts inferred from the current implementation

These are **observed client-side shapes**, not yet approved server API contracts.

### Service catalogue

Source: `agenda/services.json`

- Root: `schemaVersion`, `updatedAt`, `services[]`
- Service: `id`, `name`, `category`

Observed example service IDs include `consulta-general`, `asesoria`, `sesion`, `visita`, and `control`.

### Synthetic requestor catalogue

Source: `agenda/mock-requestors.json`

- Root: `schemaVersion`, `dataClassification`, `disclaimer`, `requestors[]`
- Requestor seed: `id`, `name`, `reference`
- Data classification: `SYNTHETIC_DEMO_ONLY`

### Requestor record

Observed fields created by the web client:

- `id`
- `name`
- `contact`
- `note`
- `source` (for example `user`, `mock`, `migrated`)
- `createdAt`

### Appointment record

Observed fields created by the web client:

- `id`
- `requestorId`
- `requestorName` (denormalized display snapshot)
- `fee`
- `currency` (`CLP` or `USD`)
- `date`
- `time`
- `service` (service ID)
- `serviceName` (display snapshot)
- `status` (currently `Pendiente` or `Confirmada`)
- `createdAt`

### Payment record

Observed fields created by the web client:

- `id`
- `appointmentId`
- `amount`
- `currency` (`CLP` or `USD`)
- `date`
- `reference`

Observed business rules:

- Payments are manually recorded; no bank integration or payment processing exists.
- Payments are associated with an appointment.
- The paid amount is the sum of payments for an appointment.
- Balance is `max(0, agreed fee - paid amount)`.
- A payment cannot exceed the outstanding balance in the current UI.
- CLP amounts are whole numbers; USD permits decimal amounts.
- The UI displays pending, partial-payment (`Abono`) and paid states derived from payment records.
- Currency totals are kept separate; no exchange-rate conversion is performed.

### Backup formats

- Empty template: `format: agenda-template-v1`, `schemaVersion: 1`, `appointments[]`, `requestors[]`.
- Backup: `format: arigato-backup-v4`, `schemaVersion: 4`, `exportedAt`, `appointments[]`, `requestors[]`, `payments[]`.

These formats must remain import-compatible during the migration. A migration adapter should be designed and tested before remote persistence becomes the default.

## 6. Functional modules observed

1. Agenda/calendar: month, week and day views; create appointment by selecting a calendar slot or opening the form.
2. People/requestors: create, list and delete requestors; optional contact and note; terminology preference.
3. Service catalogue: fetched from static JSON; read-only; local fallback exists.
4. Payments: manual payment entry, pending balances, payment history, CLP/USD totals and CSV export.
5. Portability: JSON import/export, empty template, print-to-PDF and downloadable demo ZIP.
6. Preferences: Spanish/English, theme selection and requestor terminology.
7. Demo data: synthetic requestors are loaded from a public JSON file and can be removed.

The app warns users not to store sensitive or clinical information in the public demo. The first remote backend must preserve that boundary and must not treat public demo records as real customer data.

## 7. Migration gaps and decisions required

| Area | Finding | Required discovery / action |
|---|---|---|
| Dynamic REST API | None observed | Define versioned Spring Boot API from existing client behaviour |
| Database | No schema/connection details in this repository | Inspect the actual existing database before designing entities or migrations |
| Authentication | No login/session in current demo | Decide whether v1 remains single-user/private or introduces authentication |
| Ownership/tenancy | Not represented in current local model | Define account/owner boundary before remote multi-user access |
| Concurrency | Browser-local only | Define conflict and optimistic-lock strategy for remote writes |
| Payment integrity | UI-only validation | Enforce amount, currency and balance rules server-side with transactions |
| Privacy | Demo is explicitly synthetic/local | Define retention, access controls and data classification before real records |
| Hosting | GitHub Pages serves static site only | Select a separate Java-capable remote host; keep the web app deploy independent |
| API compatibility | No OpenAPI contract exists | Publish OpenAPI as the canonical contract and test it from Playwright/Karate |

## 8. Proposed implementation sequence

### Phase 0 — Inventory and contract freeze
- Preserve `master` and all existing snapshots.
- Reconcile release/version metadata.
- Inspect the existing remote database schema and confirm access method.
- Convert observed client-side data shapes into reviewed domain schemas.
- Draft OpenAPI 3 contract; do not invent endpoints before domain review.
- Define JSON v1–v4 import/export compatibility tests.

### Phase 1 — Java 17 backend
- Add isolated Spring Boot service under the platform workspace.
- Implement domain services for people, services, appointments and payments.
- Add repository layer against the existing database only after schema inspection.
- Add validation, transaction boundaries, error model, health endpoint and OpenAPI.
- Keep public GitHub Pages demo working during parallel development.

### Phase 2 — Web integration and Playwright
- Add API client adapter to the existing web app in an isolated iteration.
- Preserve local-first mode until remote API parity and backup/restore are proven.
- Add Playwright TypeScript UI, API, migration and regression tests.
- Verify payment invariants, CLP/USD separation and calendar behaviour.

### Phase 3 — React Native mobile
- Build iOS/Android client against the same OpenAPI contract.
- Reuse domain semantics, not browser storage or web-specific components.
- Add platform accessibility IDs and deterministic test hooks.
- Keep mobile and web clients independently deployable.

### Phase 4 — Mobile automation
- Use Appium Java Client directly for native UI sessions.
- Use Karate Java for API contract, setup and integration tests.
- Share API test data conventions and environment configuration.
- Execute equivalent appointment and payment journeys on iOS and Android.

### Phase 5 — Release
- Separate semantic versions for backend, web, mobile, Playwright and mobile automation.
- Retain prior releases and migration notes.
- Require regression evidence before routing production traffic to the new backend.

## 9. Safety and preservation rules

- Do not overwrite `agenda/index.html`, `agenda/current/index.html`, historic snapshots or payment lab iterations during foundation work.
- Do not infer or expose database credentials. Use environment variables/secrets and least-privilege database access.
- Do not seed production with synthetic people or appointment/payment records.
- Do not make remote persistence the default until backup/restore and migration regression tests pass.
- Keep public demo data synthetic and clearly labelled.
- Use a feature branch and pull request for platform changes; do not commit migration work directly to `master`.

## 10. Current inventory conclusion

The repository contains a functioning local-first ARIGATO web prototype and useful static JSON catalogues. It does **not** currently contain a Java backend, a dynamic ARIGATO REST API, or a verified remote database integration. The first engineering task is therefore a controlled backend introduction based on the actual existing database and the observed browser data contracts—not a migration of an already existing REST API.
