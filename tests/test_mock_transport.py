"""No-network round-trip through httpx.MockTransport.

Asserts a generated endpoint builds the right HTTP request (method, path,
query, bearer header) and parses the JSON response into its typed model,
for both the sync and asyncio call styles.
"""

import asyncio
import json
from uuid import UUID

import httpx

from recurso import AuthenticatedClient
from recurso.api.payments import list_payment_attempts
from recurso.models import (
    ListPaymentAttemptsResponse200,
    ListPaymentAttemptsResponse200DataItemStatus,
    ListPaymentAttemptsStatus,
)

ATTEMPT_ID = UUID("11111111-1111-1111-1111-111111111111")
INVOICE_ID = UUID("22222222-2222-2222-2222-222222222222")

FIXTURE = {
    "data": [
        {
            "id": str(ATTEMPT_ID),
            "invoice_id": str(INVOICE_ID),
            "invoice_number": "INV-0001",
            "currency": "USD",
            "gateway": "stripe",
            "method": "card",
            "status": "failed",
            "failure_code": "card_declined",
            "amount": 2900,
            "created_at": "2026-09-01T10:00:00Z",
            "settled_at": None,
        }
    ],
    "pagination": {"page": 1, "per_page": 25, "total": 1, "total_pages": 1},
}


def _make_client(seen: list[httpx.Request]) -> AuthenticatedClient:
    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return httpx.Response(200, json=FIXTURE)

    return AuthenticatedClient(
        base_url="https://api.recurso.test",
        token="rsk_test_key",
        httpx_args={"transport": httpx.MockTransport(handler)},
    )


def _assert_request(request: httpx.Request) -> None:
    assert request.method == "GET"
    assert request.url.host == "api.recurso.test"
    assert request.url.path == "/v1/payment-attempts"
    assert dict(request.url.params) == {"status": "failed", "per_page": "25"}
    assert request.headers["Authorization"] == "Bearer rsk_test_key"


def _assert_parsed(parsed: ListPaymentAttemptsResponse200) -> None:
    assert isinstance(parsed, ListPaymentAttemptsResponse200)
    (item,) = parsed.data
    assert item.id == ATTEMPT_ID
    assert item.invoice_id == INVOICE_ID
    assert item.amount == 2900
    assert item.status is ListPaymentAttemptsResponse200DataItemStatus.FAILED
    assert item.created_at.isoformat() == "2026-09-01T10:00:00+00:00"
    assert item.settled_at is None
    assert parsed.pagination.total_pages == 1
    # Round-trip: the model serializes back to the wire shape.
    assert json.loads(json.dumps(parsed.to_dict()))["data"][0]["status"] == "failed"


def test_list_payment_attempts_sync_round_trip():
    seen: list[httpx.Request] = []
    client = _make_client(seen)
    with client:
        detailed = list_payment_attempts.sync_detailed(
            client=client, status=ListPaymentAttemptsStatus.FAILED, per_page=25
        )
    assert detailed.status_code == 200
    assert len(seen) == 1
    _assert_request(seen[0])
    _assert_parsed(detailed.parsed)


def test_list_payment_attempts_asyncio_round_trip():
    seen: list[httpx.Request] = []
    client = _make_client(seen)

    async def call():
        async with client:
            return await list_payment_attempts.asyncio(
                client=client, status=ListPaymentAttemptsStatus.FAILED, per_page=25
            )

    # Plain asyncio.run keeps the suite free of a pytest-asyncio dependency.
    parsed = asyncio.run(call())
    assert len(seen) == 1
    _assert_request(seen[0])
    _assert_parsed(parsed)
