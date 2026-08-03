from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.commit_stripe_import_body import CommitStripeImportBody
from ...models.commit_stripe_import_response_200 import CommitStripeImportResponse200
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    *,
    body: CommitStripeImportBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/import/stripe/commit",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CommitStripeImportResponse200 | Error | None:
    if response.status_code == 200:
        response_200 = CommitStripeImportResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CommitStripeImportResponse200 | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CommitStripeImportBody,
) -> Response[CommitStripeImportResponse200 | Error]:
    """Import a Stripe export (customers, plans, subscriptions)

     Imports the uploaded Stripe export, creating customers, plans, and subscriptions and recording an
    idempotency mapping for each. Re-running is safe: already-imported ids and records that already
    exist (by email or plan code) are skipped. Subscriptions are imported in their current billing state
    via a direct insert — no invoice, charge, or ledger entry is generated, so Recurso takes over at the
    next renewal instead of re-billing the current cycle. Per-object failures are returned in the
    response rather than aborting the whole import. Card payment methods are NOT imported — card data
    can't be migrated from a static export.

    Args:
        body (CommitStripeImportBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CommitStripeImportResponse200 | Error]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: CommitStripeImportBody,
) -> CommitStripeImportResponse200 | Error | None:
    """Import a Stripe export (customers, plans, subscriptions)

     Imports the uploaded Stripe export, creating customers, plans, and subscriptions and recording an
    idempotency mapping for each. Re-running is safe: already-imported ids and records that already
    exist (by email or plan code) are skipped. Subscriptions are imported in their current billing state
    via a direct insert — no invoice, charge, or ledger entry is generated, so Recurso takes over at the
    next renewal instead of re-billing the current cycle. Per-object failures are returned in the
    response rather than aborting the whole import. Card payment methods are NOT imported — card data
    can't be migrated from a static export.

    Args:
        body (CommitStripeImportBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CommitStripeImportResponse200 | Error
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CommitStripeImportBody,
) -> Response[CommitStripeImportResponse200 | Error]:
    """Import a Stripe export (customers, plans, subscriptions)

     Imports the uploaded Stripe export, creating customers, plans, and subscriptions and recording an
    idempotency mapping for each. Re-running is safe: already-imported ids and records that already
    exist (by email or plan code) are skipped. Subscriptions are imported in their current billing state
    via a direct insert — no invoice, charge, or ledger entry is generated, so Recurso takes over at the
    next renewal instead of re-billing the current cycle. Per-object failures are returned in the
    response rather than aborting the whole import. Card payment methods are NOT imported — card data
    can't be migrated from a static export.

    Args:
        body (CommitStripeImportBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CommitStripeImportResponse200 | Error]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CommitStripeImportBody,
) -> CommitStripeImportResponse200 | Error | None:
    """Import a Stripe export (customers, plans, subscriptions)

     Imports the uploaded Stripe export, creating customers, plans, and subscriptions and recording an
    idempotency mapping for each. Re-running is safe: already-imported ids and records that already
    exist (by email or plan code) are skipped. Subscriptions are imported in their current billing state
    via a direct insert — no invoice, charge, or ledger entry is generated, so Recurso takes over at the
    next renewal instead of re-billing the current cycle. Per-object failures are returned in the
    response rather than aborting the whole import. Card payment methods are NOT imported — card data
    can't be migrated from a static export.

    Args:
        body (CommitStripeImportBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CommitStripeImportResponse200 | Error
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
