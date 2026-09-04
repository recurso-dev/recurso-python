# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.11.0] - 2026-09-03

### Added

- Accounting / finance drill-down endpoints that landed in the API after 1.10.0
  (all 15 previously uncovered spec paths, generated with
  openapi-python-client 0.29.1 and normalized to the existing module style):
  - `recurso.api.metering.get_metric_charges` — `GET /v1/billable-metrics/{id}/charges`
  - `recurso.api.credit_notes.get_credit_note_journal_entries` — `GET /v1/credit-notes/{id}/journal-entries`
  - `recurso.api.customers.get_customer_financial_summary` — `GET /v1/customers/{id}/financial-summary`
  - `recurso.api.disputes.get_dispute` — `GET /v1/disputes/{id}`
  - `recurso.api.finance.list_reconciliation_runs` / `record_reconciliation` — `GET`/`POST /v1/finance/reconciliation/runs`
  - `recurso.api.finance.get_reconciliation_run` — `GET /v1/finance/reconciliation/runs/{id}`
  - `recurso.api.invoices.get_invoice_journal_entries` — `GET /v1/invoices/{id}/journal-entries`
  - `recurso.api.invoices.get_invoice_payment_attempts` — `GET /v1/invoices/{id}/payment-attempts`
  - `recurso.api.invoices.get_invoice_status_history` — `GET /v1/invoices/{id}/status-history`
  - `recurso.api.finance.get_ledger_transaction` — `GET /v1/ledger/transactions/{id}`
  - `recurso.api.payments.list_payment_attempts` — `GET /v1/payment-attempts` (filters: `status`, `q`, `page`, `per_page`)
  - `recurso.api.payments.get_payment_attempt` — `GET /v1/payment-attempts/{id}`
  - `recurso.api.subscriptions.get_subscription_cancel_preview` — `GET /v1/subscriptions/{id}/cancel-preview` (`immediately`)
  - `recurso.api.subscriptions.get_subscription_financial_summary` — `GET /v1/subscriptions/{id}/financial-summary`
  - `recurso.api.subscriptions.get_subscription_history` — `GET /v1/subscriptions/{id}/history`
- `recurso.api.coupons.get_coupon` — `GET /v1/coupons/{id}` (a new verb on an already-covered path).
- 45 response models under `recurso.models` for the endpoints above (e.g.
  `ListPaymentAttemptsResponse200`, `GetReconciliationRunResponse200`,
  `GetSubscriptionHistoryResponse200DataHistoryItemChangeType`).
- GitHub Actions CI (`.github/workflows/ci.yml`): on push and pull request,
  Python 3.11 and 3.12, runs `tests/smoke_test.py` and `pytest`.
- `tests/test_smoke.py` (pytest entry point for the smoke test) and
  `tests/test_mock_transport.py` (an `httpx.MockTransport` round-trip that
  asserts the request method/URL/query and response parsing without network).

### Changed

- `ReconciliationReport` gained the optional `reporting_currency` field the
  API now returns.

## [1.10.0] - 2026-08

- Previous release; see the git history for earlier changes.

[Unreleased]: https://github.com/recurso-dev/recurso-python/compare/v1.11.0...HEAD
[1.11.0]: https://github.com/recurso-dev/recurso-python/compare/v1.10.0...v1.11.0
[1.10.0]: https://github.com/recurso-dev/recurso-python/releases/tag/v1.10.0
