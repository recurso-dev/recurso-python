from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_wallet_body import CreateWalletBody
from ...models.create_wallet_response_201 import CreateWalletResponse201
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    *,
    body: CreateWalletBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/wallets",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | CreateWalletResponse201 | Error | None:
    if response.status_code == 201:
        response_201 = CreateWalletResponse201.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 409:
        response_409 = cast(Any, None)
        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | CreateWalletResponse201 | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateWalletBody,
) -> Response[Any | CreateWalletResponse201 | Error]:
    """Create a prepaid wallet

     One wallet per customer+currency, holding money-denominated balance (minor units). At invoice time
    the wallet drains FIRST — before adjustment credit notes and before the payment gateway.

    Args:
        body (CreateWalletBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateWalletResponse201 | Error]
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
    body: CreateWalletBody,
) -> Any | CreateWalletResponse201 | Error | None:
    """Create a prepaid wallet

     One wallet per customer+currency, holding money-denominated balance (minor units). At invoice time
    the wallet drains FIRST — before adjustment credit notes and before the payment gateway.

    Args:
        body (CreateWalletBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateWalletResponse201 | Error
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateWalletBody,
) -> Response[Any | CreateWalletResponse201 | Error]:
    """Create a prepaid wallet

     One wallet per customer+currency, holding money-denominated balance (minor units). At invoice time
    the wallet drains FIRST — before adjustment credit notes and before the payment gateway.

    Args:
        body (CreateWalletBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateWalletResponse201 | Error]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateWalletBody,
) -> Any | CreateWalletResponse201 | Error | None:
    """Create a prepaid wallet

     One wallet per customer+currency, holding money-denominated balance (minor units). At invoice time
    the wallet drains FIRST — before adjustment credit notes and before the payment gateway.

    Args:
        body (CreateWalletBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateWalletResponse201 | Error
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
