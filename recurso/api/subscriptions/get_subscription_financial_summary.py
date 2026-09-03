from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_subscription_financial_summary_response_200 import GetSubscriptionFinancialSummaryResponse200
from ...types import Response


def _get_kwargs(
    id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/subscriptions/{id}/financial-summary".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetSubscriptionFinancialSummaryResponse200 | None:
    if response.status_code == 200:
        response_200 = GetSubscriptionFinancialSummaryResponse200.from_dict(response.json())

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
) -> Response[Any | GetSubscriptionFinancialSummaryResponse200]:
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
) -> Response[Any | GetSubscriptionFinancialSummaryResponse200]:
    """Subscription financial summary

     One subscription's financial position: MRR (monthly-normalized list price, counted only when active
    — 0 otherwise, matching the tenant-wide MRR definition), the recurring list price + interval, the
    next-invoice date and base amount when it will renew (base = list price only; it excludes
    tax/coupon/add-ons/usage), and its invoice-derived outstanding position per currency. Read-only;
    cross-tenant ids return 404.

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSubscriptionFinancialSummaryResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetSubscriptionFinancialSummaryResponse200 | None:
    """Subscription financial summary

     One subscription's financial position: MRR (monthly-normalized list price, counted only when active
    — 0 otherwise, matching the tenant-wide MRR definition), the recurring list price + interval, the
    next-invoice date and base amount when it will renew (base = list price only; it excludes
    tax/coupon/add-ons/usage), and its invoice-derived outstanding position per currency. Read-only;
    cross-tenant ids return 404.

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSubscriptionFinancialSummaryResponse200
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GetSubscriptionFinancialSummaryResponse200]:
    """Subscription financial summary

     One subscription's financial position: MRR (monthly-normalized list price, counted only when active
    — 0 otherwise, matching the tenant-wide MRR definition), the recurring list price + interval, the
    next-invoice date and base amount when it will renew (base = list price only; it excludes
    tax/coupon/add-ons/usage), and its invoice-derived outstanding position per currency. Read-only;
    cross-tenant ids return 404.

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSubscriptionFinancialSummaryResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetSubscriptionFinancialSummaryResponse200 | None:
    """Subscription financial summary

     One subscription's financial position: MRR (monthly-normalized list price, counted only when active
    — 0 otherwise, matching the tenant-wide MRR definition), the recurring list price + interval, the
    next-invoice date and base amount when it will renew (base = list price only; it excludes
    tax/coupon/add-ons/usage), and its invoice-derived outstanding position per currency. Read-only;
    cross-tenant ids return 404.

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSubscriptionFinancialSummaryResponse200
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
