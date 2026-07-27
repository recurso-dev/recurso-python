from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.close_wallet_response_200 import CloseWalletResponse200
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/wallets/{id}/close".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CloseWalletResponse200 | Error | None:
    if response.status_code == 200:
        response_200 = CloseWalletResponse200.from_dict(response.json())

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
) -> Response[CloseWalletResponse200 | Error]:
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
) -> Response[CloseWalletResponse200 | Error]:
    """Close a wallet and settle its balance

     Closes the wallet: paid residue is refunded to the customer, promotional residue is forfeited (non-
    refundable), and the ledger legs are posted (DR Customer Credit / CR Cash for the refund; DR
    Customer Credit / CR Credits for the forfeit). A closed wallet accepts no further top-ups or drains.
    `refunded` is the amount owed back to the customer; the actual money return is handled out of band,
    like a manual refund.

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CloseWalletResponse200 | Error]
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
) -> CloseWalletResponse200 | Error | None:
    """Close a wallet and settle its balance

     Closes the wallet: paid residue is refunded to the customer, promotional residue is forfeited (non-
    refundable), and the ledger legs are posted (DR Customer Credit / CR Cash for the refund; DR
    Customer Credit / CR Credits for the forfeit). A closed wallet accepts no further top-ups or drains.
    `refunded` is the amount owed back to the customer; the actual money return is handled out of band,
    like a manual refund.

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CloseWalletResponse200 | Error
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[CloseWalletResponse200 | Error]:
    """Close a wallet and settle its balance

     Closes the wallet: paid residue is refunded to the customer, promotional residue is forfeited (non-
    refundable), and the ledger legs are posted (DR Customer Credit / CR Cash for the refund; DR
    Customer Credit / CR Credits for the forfeit). A closed wallet accepts no further top-ups or drains.
    `refunded` is the amount owed back to the customer; the actual money return is handled out of band,
    like a manual refund.

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CloseWalletResponse200 | Error]
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
) -> CloseWalletResponse200 | Error | None:
    """Close a wallet and settle its balance

     Closes the wallet: paid residue is refunded to the customer, promotional residue is forfeited (non-
    refundable), and the ledger legs are posted (DR Customer Credit / CR Cash for the refund; DR
    Customer Credit / CR Credits for the forfeit). A closed wallet accepts no further top-ups or drains.
    `refunded` is the amount owed back to the customer; the actual money return is handled out of band,
    like a manual refund.

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CloseWalletResponse200 | Error
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
