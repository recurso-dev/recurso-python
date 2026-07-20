from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.connect_accounting_provider_token_body import ConnectAccountingProviderTokenBody
from ...models.connect_accounting_provider_token_provider import ConnectAccountingProviderTokenProvider
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    provider: ConnectAccountingProviderTokenProvider,
    *,
    body: ConnectAccountingProviderTokenBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/accounting/connect-token/{provider}".format(
            provider=quote(str(provider), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Error | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 201:
        response_201 = cast(Any, None)
        return response_201

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    provider: ConnectAccountingProviderTokenProvider,
    *,
    client: AuthenticatedClient | Client,
    body: ConnectAccountingProviderTokenBody | Unset = UNSET,
) -> Response[Any | Error]:
    """Connect a token-based accounting provider (NetSuite, Tally)

     Creates or refreshes a connection for providers outside the browser OAuth flow. `netsuite` requires
    `account_id` and a SuiteTalk OAuth 2.0 `access_token` minted in NetSuite (EXPERIMENTAL). `tally`
    takes no credentials — it enables the local JSONL export sync.

    Args:
        provider (ConnectAccountingProviderTokenProvider):
        body (ConnectAccountingProviderTokenBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
    """

    kwargs = _get_kwargs(
        provider=provider,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    provider: ConnectAccountingProviderTokenProvider,
    *,
    client: AuthenticatedClient | Client,
    body: ConnectAccountingProviderTokenBody | Unset = UNSET,
) -> Any | Error | None:
    """Connect a token-based accounting provider (NetSuite, Tally)

     Creates or refreshes a connection for providers outside the browser OAuth flow. `netsuite` requires
    `account_id` and a SuiteTalk OAuth 2.0 `access_token` minted in NetSuite (EXPERIMENTAL). `tally`
    takes no credentials — it enables the local JSONL export sync.

    Args:
        provider (ConnectAccountingProviderTokenProvider):
        body (ConnectAccountingProviderTokenBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
    """

    return sync_detailed(
        provider=provider,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    provider: ConnectAccountingProviderTokenProvider,
    *,
    client: AuthenticatedClient | Client,
    body: ConnectAccountingProviderTokenBody | Unset = UNSET,
) -> Response[Any | Error]:
    """Connect a token-based accounting provider (NetSuite, Tally)

     Creates or refreshes a connection for providers outside the browser OAuth flow. `netsuite` requires
    `account_id` and a SuiteTalk OAuth 2.0 `access_token` minted in NetSuite (EXPERIMENTAL). `tally`
    takes no credentials — it enables the local JSONL export sync.

    Args:
        provider (ConnectAccountingProviderTokenProvider):
        body (ConnectAccountingProviderTokenBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
    """

    kwargs = _get_kwargs(
        provider=provider,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    provider: ConnectAccountingProviderTokenProvider,
    *,
    client: AuthenticatedClient | Client,
    body: ConnectAccountingProviderTokenBody | Unset = UNSET,
) -> Any | Error | None:
    """Connect a token-based accounting provider (NetSuite, Tally)

     Creates or refreshes a connection for providers outside the browser OAuth flow. `netsuite` requires
    `account_id` and a SuiteTalk OAuth 2.0 `access_token` minted in NetSuite (EXPERIMENTAL). `tally`
    takes no credentials — it enables the local JSONL export sync.

    Args:
        provider (ConnectAccountingProviderTokenProvider):
        body (ConnectAccountingProviderTokenBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
    """

    return (
        await asyncio_detailed(
            provider=provider,
            client=client,
            body=body,
        )
    ).parsed
