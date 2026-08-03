from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.commit_chargebee_import_body import CommitChargebeeImportBody
from ...models.commit_chargebee_import_response_200 import CommitChargebeeImportResponse200
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    *,
    body: CommitChargebeeImportBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/import/chargebee/commit",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CommitChargebeeImportResponse200 | Error | None:
    if response.status_code == 200:
        response_200 = CommitChargebeeImportResponse200.from_dict(response.json())

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
) -> Response[CommitChargebeeImportResponse200 | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CommitChargebeeImportBody,
) -> Response[CommitChargebeeImportResponse200 | Error]:
    """Import a Chargebee export (customers, plans, subscriptions)

     Imports the uploaded Chargebee export idempotently — creating customers, plans, and subscriptions
    and recording an idempotency mapping for each. Subscriptions are imported in their current billing
    state via a direct insert (no invoice/charge/ledger side effect). Re-running is safe; per-object
    failures are returned rather than aborting the import.

    Args:
        body (CommitChargebeeImportBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CommitChargebeeImportResponse200 | Error]
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
    body: CommitChargebeeImportBody,
) -> CommitChargebeeImportResponse200 | Error | None:
    """Import a Chargebee export (customers, plans, subscriptions)

     Imports the uploaded Chargebee export idempotently — creating customers, plans, and subscriptions
    and recording an idempotency mapping for each. Subscriptions are imported in their current billing
    state via a direct insert (no invoice/charge/ledger side effect). Re-running is safe; per-object
    failures are returned rather than aborting the import.

    Args:
        body (CommitChargebeeImportBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CommitChargebeeImportResponse200 | Error
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CommitChargebeeImportBody,
) -> Response[CommitChargebeeImportResponse200 | Error]:
    """Import a Chargebee export (customers, plans, subscriptions)

     Imports the uploaded Chargebee export idempotently — creating customers, plans, and subscriptions
    and recording an idempotency mapping for each. Subscriptions are imported in their current billing
    state via a direct insert (no invoice/charge/ledger side effect). Re-running is safe; per-object
    failures are returned rather than aborting the import.

    Args:
        body (CommitChargebeeImportBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CommitChargebeeImportResponse200 | Error]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CommitChargebeeImportBody,
) -> CommitChargebeeImportResponse200 | Error | None:
    """Import a Chargebee export (customers, plans, subscriptions)

     Imports the uploaded Chargebee export idempotently — creating customers, plans, and subscriptions
    and recording an idempotency mapping for each. Subscriptions are imported in their current billing
    state via a direct insert (no invoice/charge/ledger side effect). Re-running is safe; per-object
    failures are returned rather than aborting the import.

    Args:
        body (CommitChargebeeImportBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CommitChargebeeImportResponse200 | Error
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
