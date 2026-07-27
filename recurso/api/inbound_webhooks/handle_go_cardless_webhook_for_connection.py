from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.handle_go_cardless_webhook_for_connection_body import HandleGoCardlessWebhookForConnectionBody
from ...models.handle_go_cardless_webhook_for_connection_response_200 import (
    HandleGoCardlessWebhookForConnectionResponse200,
)
from ...types import Response


def _get_kwargs(
    conn_id: UUID,
    *,
    body: HandleGoCardlessWebhookForConnectionBody,
    webhook_signature: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Webhook-Signature"] = webhook_signature

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/webhooks/gocardless/{conn_id}".format(
            conn_id=quote(str(conn_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | HandleGoCardlessWebhookForConnectionResponse200 | None:
    if response.status_code == 200:
        response_200 = HandleGoCardlessWebhookForConnectionResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | HandleGoCardlessWebhookForConnectionResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    conn_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: HandleGoCardlessWebhookForConnectionBody,
    webhook_signature: str,
) -> Response[Error | HandleGoCardlessWebhookForConnectionResponse200]:
    """GoCardless webhook receiver (per-connection, BYO)

     Per-connection variant of the GoCardless webhook receiver for tenants
    who connected their own GoCardless account. The batch is verified with
    THAT connection's own signing secret (resolved from `connID`) before
    any event is trusted. Called by GoCardless, not by API consumers.

    Args:
        conn_id (UUID):
        webhook_signature (str):
        body (HandleGoCardlessWebhookForConnectionBody): Raw GoCardless events payload.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | HandleGoCardlessWebhookForConnectionResponse200]
    """

    kwargs = _get_kwargs(
        conn_id=conn_id,
        body=body,
        webhook_signature=webhook_signature,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    conn_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: HandleGoCardlessWebhookForConnectionBody,
    webhook_signature: str,
) -> Error | HandleGoCardlessWebhookForConnectionResponse200 | None:
    """GoCardless webhook receiver (per-connection, BYO)

     Per-connection variant of the GoCardless webhook receiver for tenants
    who connected their own GoCardless account. The batch is verified with
    THAT connection's own signing secret (resolved from `connID`) before
    any event is trusted. Called by GoCardless, not by API consumers.

    Args:
        conn_id (UUID):
        webhook_signature (str):
        body (HandleGoCardlessWebhookForConnectionBody): Raw GoCardless events payload.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | HandleGoCardlessWebhookForConnectionResponse200
    """

    return sync_detailed(
        conn_id=conn_id,
        client=client,
        body=body,
        webhook_signature=webhook_signature,
    ).parsed


async def asyncio_detailed(
    conn_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: HandleGoCardlessWebhookForConnectionBody,
    webhook_signature: str,
) -> Response[Error | HandleGoCardlessWebhookForConnectionResponse200]:
    """GoCardless webhook receiver (per-connection, BYO)

     Per-connection variant of the GoCardless webhook receiver for tenants
    who connected their own GoCardless account. The batch is verified with
    THAT connection's own signing secret (resolved from `connID`) before
    any event is trusted. Called by GoCardless, not by API consumers.

    Args:
        conn_id (UUID):
        webhook_signature (str):
        body (HandleGoCardlessWebhookForConnectionBody): Raw GoCardless events payload.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | HandleGoCardlessWebhookForConnectionResponse200]
    """

    kwargs = _get_kwargs(
        conn_id=conn_id,
        body=body,
        webhook_signature=webhook_signature,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    conn_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: HandleGoCardlessWebhookForConnectionBody,
    webhook_signature: str,
) -> Error | HandleGoCardlessWebhookForConnectionResponse200 | None:
    """GoCardless webhook receiver (per-connection, BYO)

     Per-connection variant of the GoCardless webhook receiver for tenants
    who connected their own GoCardless account. The batch is verified with
    THAT connection's own signing secret (resolved from `connID`) before
    any event is trusted. Called by GoCardless, not by API consumers.

    Args:
        conn_id (UUID):
        webhook_signature (str):
        body (HandleGoCardlessWebhookForConnectionBody): Raw GoCardless events payload.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | HandleGoCardlessWebhookForConnectionResponse200
    """

    return (
        await asyncio_detailed(
            conn_id=conn_id,
            client=client,
            body=body,
            webhook_signature=webhook_signature,
        )
    ).parsed
