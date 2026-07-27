from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.handle_stripe_webhook_for_connection_body import HandleStripeWebhookForConnectionBody
from ...models.handle_stripe_webhook_for_connection_response_200 import HandleStripeWebhookForConnectionResponse200
from typing import cast
from uuid import UUID



def _get_kwargs(
    conn_id: UUID,
    *,
    body: HandleStripeWebhookForConnectionBody,
    stripe_signature: str,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Stripe-Signature"] = stripe_signature



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/webhooks/stripe/{conn_id}".format(conn_id=quote(str(conn_id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | HandleStripeWebhookForConnectionResponse200 | None:
    if response.status_code == 200:
        response_200 = HandleStripeWebhookForConnectionResponse200.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | HandleStripeWebhookForConnectionResponse200]:
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
    body: HandleStripeWebhookForConnectionBody,
    stripe_signature: str,

) -> Response[Error | HandleStripeWebhookForConnectionResponse200]:
    """ Stripe webhook receiver (per-connection, BYO)

     Per-connection variant of the Stripe webhook receiver for tenants who
    connected their own Stripe account. The event is verified with THAT
    connection's own signing secret (resolved from `connID`) before the
    payload is trusted. Called by Stripe, not by API consumers.

    Args:
        conn_id (UUID):
        stripe_signature (str):
        body (HandleStripeWebhookForConnectionBody): Raw Stripe event payload.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | HandleStripeWebhookForConnectionResponse200]
     """


    kwargs = _get_kwargs(
        conn_id=conn_id,
body=body,
stripe_signature=stripe_signature,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    conn_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: HandleStripeWebhookForConnectionBody,
    stripe_signature: str,

) -> Error | HandleStripeWebhookForConnectionResponse200 | None:
    """ Stripe webhook receiver (per-connection, BYO)

     Per-connection variant of the Stripe webhook receiver for tenants who
    connected their own Stripe account. The event is verified with THAT
    connection's own signing secret (resolved from `connID`) before the
    payload is trusted. Called by Stripe, not by API consumers.

    Args:
        conn_id (UUID):
        stripe_signature (str):
        body (HandleStripeWebhookForConnectionBody): Raw Stripe event payload.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | HandleStripeWebhookForConnectionResponse200
     """


    return sync_detailed(
        conn_id=conn_id,
client=client,
body=body,
stripe_signature=stripe_signature,

    ).parsed

async def asyncio_detailed(
    conn_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: HandleStripeWebhookForConnectionBody,
    stripe_signature: str,

) -> Response[Error | HandleStripeWebhookForConnectionResponse200]:
    """ Stripe webhook receiver (per-connection, BYO)

     Per-connection variant of the Stripe webhook receiver for tenants who
    connected their own Stripe account. The event is verified with THAT
    connection's own signing secret (resolved from `connID`) before the
    payload is trusted. Called by Stripe, not by API consumers.

    Args:
        conn_id (UUID):
        stripe_signature (str):
        body (HandleStripeWebhookForConnectionBody): Raw Stripe event payload.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | HandleStripeWebhookForConnectionResponse200]
     """


    kwargs = _get_kwargs(
        conn_id=conn_id,
body=body,
stripe_signature=stripe_signature,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    conn_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: HandleStripeWebhookForConnectionBody,
    stripe_signature: str,

) -> Error | HandleStripeWebhookForConnectionResponse200 | None:
    """ Stripe webhook receiver (per-connection, BYO)

     Per-connection variant of the Stripe webhook receiver for tenants who
    connected their own Stripe account. The event is verified with THAT
    connection's own signing secret (resolved from `connID`) before the
    payload is trusted. Called by Stripe, not by API consumers.

    Args:
        conn_id (UUID):
        stripe_signature (str):
        body (HandleStripeWebhookForConnectionBody): Raw Stripe event payload.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | HandleStripeWebhookForConnectionResponse200
     """


    return (await asyncio_detailed(
        conn_id=conn_id,
client=client,
body=body,
stripe_signature=stripe_signature,

    )).parsed
