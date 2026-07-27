from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.sync_crm_now_response_200 import SyncCRMNowResponse200
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/crm/sync",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | Error | SyncCRMNowResponse200 | None:
    if response.status_code == 200:
        response_200 = SyncCRMNowResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 424:
        response_424 = cast(Any, None)
        return response_424

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | Error | SyncCRMNowResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | Error | SyncCRMNowResponse200]:
    """Sync this workspace's customers to its connected CRM now

     Runs the CRM sweep for the calling workspace synchronously — the way to test a freshly connected
    HubSpot token instead of waiting for the daily sweep. Returns how many contacts were upserted. 400
    when no CRM is connected; 502 carries the provider's own rejection (bad token, missing scopes).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error | SyncCRMNowResponse200]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> Any | Error | SyncCRMNowResponse200 | None:
    """Sync this workspace's customers to its connected CRM now

     Runs the CRM sweep for the calling workspace synchronously — the way to test a freshly connected
    HubSpot token instead of waiting for the daily sweep. Returns how many contacts were upserted. 400
    when no CRM is connected; 502 carries the provider's own rejection (bad token, missing scopes).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error | SyncCRMNowResponse200
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | Error | SyncCRMNowResponse200]:
    """Sync this workspace's customers to its connected CRM now

     Runs the CRM sweep for the calling workspace synchronously — the way to test a freshly connected
    HubSpot token instead of waiting for the daily sweep. Returns how many contacts were upserted. 400
    when no CRM is connected; 502 carries the provider's own rejection (bad token, missing scopes).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error | SyncCRMNowResponse200]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> Any | Error | SyncCRMNowResponse200 | None:
    """Sync this workspace's customers to its connected CRM now

     Runs the CRM sweep for the calling workspace synchronously — the way to test a freshly connected
    HubSpot token instead of waiting for the daily sweep. Returns how many contacts were upserted. 400
    when no CRM is connected; 502 carries the provider's own rejection (bad token, missing scopes).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error | SyncCRMNowResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
