from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_subscription_cancel_preview_response_200 import GetSubscriptionCancelPreviewResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: UUID,
    *,
    immediately: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["immediately"] = immediately

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/subscriptions/{id}/cancel-preview".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetSubscriptionCancelPreviewResponse200 | None:
    if response.status_code == 200:
        response_200 = GetSubscriptionCancelPreviewResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GetSubscriptionCancelPreviewResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    immediately: bool | Unset = False,
) -> Response[Any | GetSubscriptionCancelPreviewResponse200]:
    """Preview the financial consequence of a cancellation

     The deterministic financial forecast of canceling a subscription, shown BEFORE the mutation so an
    operator never cancels blind. Exposes only what the engine computes deterministically: effective
    time + resulting status, the still-deferred revenue an immediate cancel forfeits and recognizes as
    breakage (computed read-only from the same rev-rec data the mutation uses), the future recurring
    amount that will no longer bill, and flat_fee_refund (constant 0 — the flat fee is paid in advance,
    not refunded). It deliberately omits an unused-time proration credit (the cancel mutation posts
    none) and a final metered-usage figure (only the mutating invoice path can produce it). The cancel
    mutation is unchanged. Read-only; cross-tenant ids return 404.

    Args:
        id (UUID):
        immediately (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSubscriptionCancelPreviewResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        immediately=immediately,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    immediately: bool | Unset = False,
) -> Any | GetSubscriptionCancelPreviewResponse200 | None:
    """Preview the financial consequence of a cancellation

     The deterministic financial forecast of canceling a subscription, shown BEFORE the mutation so an
    operator never cancels blind. Exposes only what the engine computes deterministically: effective
    time + resulting status, the still-deferred revenue an immediate cancel forfeits and recognizes as
    breakage (computed read-only from the same rev-rec data the mutation uses), the future recurring
    amount that will no longer bill, and flat_fee_refund (constant 0 — the flat fee is paid in advance,
    not refunded). It deliberately omits an unused-time proration credit (the cancel mutation posts
    none) and a final metered-usage figure (only the mutating invoice path can produce it). The cancel
    mutation is unchanged. Read-only; cross-tenant ids return 404.

    Args:
        id (UUID):
        immediately (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSubscriptionCancelPreviewResponse200
    """

    return sync_detailed(
        id=id,
        client=client,
        immediately=immediately,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    immediately: bool | Unset = False,
) -> Response[Any | GetSubscriptionCancelPreviewResponse200]:
    """Preview the financial consequence of a cancellation

     The deterministic financial forecast of canceling a subscription, shown BEFORE the mutation so an
    operator never cancels blind. Exposes only what the engine computes deterministically: effective
    time + resulting status, the still-deferred revenue an immediate cancel forfeits and recognizes as
    breakage (computed read-only from the same rev-rec data the mutation uses), the future recurring
    amount that will no longer bill, and flat_fee_refund (constant 0 — the flat fee is paid in advance,
    not refunded). It deliberately omits an unused-time proration credit (the cancel mutation posts
    none) and a final metered-usage figure (only the mutating invoice path can produce it). The cancel
    mutation is unchanged. Read-only; cross-tenant ids return 404.

    Args:
        id (UUID):
        immediately (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSubscriptionCancelPreviewResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        immediately=immediately,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    immediately: bool | Unset = False,
) -> Any | GetSubscriptionCancelPreviewResponse200 | None:
    """Preview the financial consequence of a cancellation

     The deterministic financial forecast of canceling a subscription, shown BEFORE the mutation so an
    operator never cancels blind. Exposes only what the engine computes deterministically: effective
    time + resulting status, the still-deferred revenue an immediate cancel forfeits and recognizes as
    breakage (computed read-only from the same rev-rec data the mutation uses), the future recurring
    amount that will no longer bill, and flat_fee_refund (constant 0 — the flat fee is paid in advance,
    not refunded). It deliberately omits an unused-time proration credit (the cancel mutation posts
    none) and a final metered-usage figure (only the mutating invoice path can produce it). The cancel
    mutation is unchanged. Read-only; cross-tenant ids return 404.

    Args:
        id (UUID):
        immediately (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSubscriptionCancelPreviewResponse200
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            immediately=immediately,
        )
    ).parsed
