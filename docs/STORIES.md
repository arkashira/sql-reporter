# STORIES.md – sql‑reporter

## Overview
**Product:** sql‑reporter – a self‑service SQL query platform that enables business users to create, schedule, and share data‑driven reports without needing data‑engineer assistance.  

**Goal:** Deliver a Minimum Viable Product (MVP) that lets non‑technical users run safe, governed queries, export results, and collaborate on dashboards, while providing admins with robust security, monitoring, and cost‑control features.

---

## Epic 1 – Core Query Engine & UI (MVP)

| # | User Story | Acceptance Criteria |
|---|------------|----------------------|
| 1 | **As a Business Analyst, I want a web UI where I can write and run SQL queries against our data warehouse, so that I can explore data on my own.** | - UI displays a syntax‑highlighted editor (Monaco/CodeMirror).<br>- “Run” button executes the query and shows results in a paginated table.<br>- Query execution respects the user’s data‑access permissions.<br>- Errors are shown with clear messages (syntax, permission, timeout). |
| 2 | **As a Business Analyst, I want to save a query with a friendly name, so that I can reuse it later without re‑typing.** | - “Save Query” dialog prompts for name, description, and optional tags.<br>- Saved queries appear in a “My Queries” list.<br>- Saved query can be opened, edited, and re‑run. |
| 3 | **As a Business Analyst, I want to export query results to CSV/Excel, so that I can share raw data with stakeholders.** | - Export button available on result table.<br>- CSV conforms to RFC 4180; Excel export uses .xlsx with proper data types.<br>- Export respects row‑limit settings (default 10 k rows, configurable). |
| 4 | **As a Business Analyst, I want to preview query performance (estimated rows, runtime), so that I can avoid costly long‑running queries.** | - UI shows an estimated row count and cost estimate before execution (using warehouse EXPLAIN or statistics).<br>- Warning displayed if estimate exceeds admin‑defined thresholds. |

---

## Epic 2 – Governance, Security & Auditing

| # | User Story | Acceptance Criteria |
|---|------------|----------------------|
| 5 | **As a Data Engineer, I want to define role‑based access controls (RBAC) for schemas/tables, so that users only see data they’re authorized to.** | - Admin UI to map Axentx roles → warehouse permissions (schema, table, column).<br>- Query engine enforces RBAC at compile time (rejects unauthorized references). |
| 6 | **As a Compliance Officer, I want an audit log of every query run, who ran it, and its outcome, so that we can meet regulatory requirements.** | - Immutable log stored in a secure audit table (query_id, user_id, timestamp, sql_text, status, row_count, duration).<br>- Log searchable via admin UI with filters (date, user, status). |
| 7 | **As a Data Engineer, I want to set maximum runtime and row‑return limits per role, so that runaway queries don’t impact the warehouse.** | - Configurable limits (e.g., 5 min, 1 M rows) per role.<br>- Queries exceeding limits are cancelled and flagged in the audit log. |

---

## Epic 3 – Reporting & Scheduling

| # | User Story | Acceptance Criteria |
|---|------------|----------------------|
| 8 | **As a Business Analyst, I want to schedule a saved query to run automatically (daily/weekly), so that I receive up‑to‑date reports without manual effort.** | - Scheduler UI lets user pick saved query, frequency, and time zone.<br>- Runs are executed as background jobs; results stored as snapshots. |
| 9 | **As a Business Analyst, I want to view scheduled query results as a dashboard widget, so that I can monitor key metrics at a glance.** | - Dashboard builder lets user add “Query Result” widgets (table or chart).<br>- Widget auto‑refreshes after each scheduled run. |
| 10 | **As a Business Analyst, I want to receive an email (or Slack) notification when a scheduled report finishes or fails, so that I stay informed.** | - Notification settings per schedule (success, failure, both).<br>- Email includes a link to the result; Slack uses a webhook payload. |

---

## Epic 4 – Collaboration & Sharing (Post‑MVP)

| # | User Story | Acceptance Criteria |
|---|------------|----------------------|
| 11 | **As a Business Analyst, I want to share a saved query or dashboard with a team, so that collaborators can view or edit it.** | - Share dialog with permission levels (view, edit).<br>- Shared objects appear in recipients’ “Shared With Me” list. |
| 12 | **As a Team Lead, I want to comment on a query result, so that I can discuss insights directly in the platform.** | - Inline comment thread attached to a result row or chart point.<br>- Notifications sent to participants. |
| 13 | **As a Data Engineer, I want to version saved queries, so that we can track changes and roll back if needed.** | - Each save creates a new version entry.<br>- UI shows version history with diff view.<br>- Ability to restore any prior version. |

---

## Epic 5 – Performance & Scalability (Infrastructure)

| # | User Story | Acceptance Criteria |
|---|------------|----------------------|
| 14 | **As a Platform Engineer, I want the query executor to use connection pooling and async execution, so that the service can handle many concurrent users.** | - Integration with `vLLM`‑style async worker pool.<br>- Metrics exposed (active queries, queue length). |
| 15 | **As a Platform Engineer, I want automated backups of saved queries and audit logs, so that data is not lost.** | - Daily snapshot to object storage (e.g., S3).<br>- Restore procedure documented and tested. |

---

## Prioritization for MVP (first release)

1. Epic 1 – Core Query Engine & UI (Stories 1‑4)  
2. Epic 2 – Governance, Security & Auditing (Stories 5‑7)  
3. Epic 3 – Reporting & Scheduling (Stories 8‑10)  

Post‑MVP work will focus on collaboration (Epic 4) and infrastructure robustness (Epic 5).

--- 

*All stories are written to be **shippable**: they include clear acceptance criteria, are testable, and map to concrete UI components or backend services within the `sql-reporter` codebase.*
