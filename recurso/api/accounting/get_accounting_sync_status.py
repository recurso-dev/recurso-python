from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.get_accounting_sync_status_response_200 import GetAccountingSyncStatusResponse200
from ...models.get_accounting_sync_status_status import GetAccountingSyncStatusStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    provider: str | Unset = UNSET,
    status: GetAccountingSyncStatusStatus | Unset = UNSET,
    search: str | Unset = UNSET,
    limit: int | Unset = 25,
    offset: int | Unset = 0,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["provider"] = provider

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params["search"] = search

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/accounting/sync/status",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | GetAccountingSyncStatusResponse200 | None:
    if response.status_code == 200:
        response_200 = GetAccountingSyncStatusResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | GetAccountingSyncStatusResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    provider: str | Unset = UNSET,
    status: GetAccountingSyncStatusStatus | Unset = UNSET,
    search: str | Unset = UNSET,
    limit: int | Unset = 25,
    offset: int | Unset = 0,
) -> Response[Error | GetAccountingSyncStatusResponse200]:
    """Recent accounting sync log

     Recent per-entity sync results, newest first (paged via limit/offset).

    Args:
        provider (str | Unset):
        status (GetAccountingSyncStatusStatus | Unset):
        search (str | Unset):
        limit (int | Unset):  Default: 25.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetAccountingSyncStatusResponse200]
    """

    kwargs = _get_kwargs(
        provider=provider,
        status=status,
        search=search,
        limit=limit,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    provider: str | Unset = UNSET,
    status: GetAccountingSyncStatusStatus | Unset = UNSET,
    search: str | Unset = UNSET,
    limit: int | Unset = 25,
    offset: int | Unset = 0,
) -> Error | GetAccountingSyncStatusResponse200 | None:
    """Recent accounting sync log

     Recent per-entity sync results, newest first (paged via limit/offset).

    Args:
        provider (str | Unset):
        status (GetAccountingSyncStatusStatus | Unset):
        search (str | Unset):
        limit (int | Unset):  Default: 25.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetAccountingSyncStatusResponse200
    """

    return sync_detailed(
        client=client,
        provider=provider,
        status=status,
        search=search,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    provider: str | Unset = UNSET,
    status: GetAccountingSyncStatusStatus | Unset = UNSET,
    search: str | Unset = UNSET,
    limit: int | Unset = 25,
    offset: int | Unset = 0,
) -> Response[Error | GetAccountingSyncStatusResponse200]:
    """Recent accounting sync log

     Recent per-entity sync results, newest first (paged via limit/offset).

    Args:
        provider (str | Unset):
        status (GetAccountingSyncStatusStatus | Unset):
        search (str | Unset):
        limit (int | Unset):  Default: 25.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetAccountingSyncStatusResponse200]
    """

    kwargs = _get_kwargs(
        provider=provider,
        status=status,
        search=search,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    provider: str | Unset = UNSET,
    status: GetAccountingSyncStatusStatus | Unset = UNSET,
    search: str | Unset = UNSET,
    limit: int | Unset = 25,
    offset: int | Unset = 0,
) -> Error | GetAccountingSyncStatusResponse200 | None:
    """Recent accounting sync log

     Recent per-entity sync results, newest first (paged via limit/offset).

    Args:
        provider (str | Unset):
        status (GetAccountingSyncStatusStatus | Unset):
        search (str | Unset):
        limit (int | Unset):  Default: 25.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetAccountingSyncStatusResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            provider=provider,
            status=status,
            search=search,
            limit=limit,
            offset=offset,
        )
    ).parsed
