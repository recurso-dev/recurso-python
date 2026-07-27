from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.handle_go_cardless_webhook_body import HandleGoCardlessWebhookBody
from ...models.handle_go_cardless_webhook_response_200 import HandleGoCardlessWebhookResponse200
from ...types import Response


def _get_kwargs(
    *,
    body: HandleGoCardlessWebhookBody,
    webhook_signature: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Webhook-Signature"] = webhook_signature

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/webhooks/gocardless",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | HandleGoCardlessWebhookResponse200 | None:
    if response.status_code == 200:
        response_200 = HandleGoCardlessWebhookResponse200.from_dict(response.json())

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
) -> Response[Error | HandleGoCardlessWebhookResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: HandleGoCardlessWebhookBody,
    webhook_signature: str,
) -> Response[Error | HandleGoCardlessWebhookResponse200]:
    """GoCardless webhook receiver (platform account)

     Receives GoCardless webhook deliveries for the platform's own
    GoCardless account. Each delivery batches multiple events; billing
    request fulfilment activates the corresponding mandate and mandate
    lifecycle events keep local status in sync. The raw body is verified
    against the `Webhook-Signature` HMAC before any event is trusted.
    Called by GoCardless, not by API consumers.

    Args:
        webhook_signature (str):
        body (HandleGoCardlessWebhookBody): Raw GoCardless events payload.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | HandleGoCardlessWebhookResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
        webhook_signature=webhook_signature,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: HandleGoCardlessWebhookBody,
    webhook_signature: str,
) -> Error | HandleGoCardlessWebhookResponse200 | None:
    """GoCardless webhook receiver (platform account)

     Receives GoCardless webhook deliveries for the platform's own
    GoCardless account. Each delivery batches multiple events; billing
    request fulfilment activates the corresponding mandate and mandate
    lifecycle events keep local status in sync. The raw body is verified
    against the `Webhook-Signature` HMAC before any event is trusted.
    Called by GoCardless, not by API consumers.

    Args:
        webhook_signature (str):
        body (HandleGoCardlessWebhookBody): Raw GoCardless events payload.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | HandleGoCardlessWebhookResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
        webhook_signature=webhook_signature,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: HandleGoCardlessWebhookBody,
    webhook_signature: str,
) -> Response[Error | HandleGoCardlessWebhookResponse200]:
    """GoCardless webhook receiver (platform account)

     Receives GoCardless webhook deliveries for the platform's own
    GoCardless account. Each delivery batches multiple events; billing
    request fulfilment activates the corresponding mandate and mandate
    lifecycle events keep local status in sync. The raw body is verified
    against the `Webhook-Signature` HMAC before any event is trusted.
    Called by GoCardless, not by API consumers.

    Args:
        webhook_signature (str):
        body (HandleGoCardlessWebhookBody): Raw GoCardless events payload.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | HandleGoCardlessWebhookResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
        webhook_signature=webhook_signature,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: HandleGoCardlessWebhookBody,
    webhook_signature: str,
) -> Error | HandleGoCardlessWebhookResponse200 | None:
    """GoCardless webhook receiver (platform account)

     Receives GoCardless webhook deliveries for the platform's own
    GoCardless account. Each delivery batches multiple events; billing
    request fulfilment activates the corresponding mandate and mandate
    lifecycle events keep local status in sync. The raw body is verified
    against the `Webhook-Signature` HMAC before any event is trusted.
    Called by GoCardless, not by API consumers.

    Args:
        webhook_signature (str):
        body (HandleGoCardlessWebhookBody): Raw GoCardless events payload.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | HandleGoCardlessWebhookResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            webhook_signature=webhook_signature,
        )
    ).parsed
