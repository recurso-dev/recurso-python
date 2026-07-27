from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.get_dunning_timing_response_200 import GetDunningTimingResponse200
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/analytics/dunning/timing",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | GetDunningTimingResponse200 | None:
    if response.status_code == 200:
        response_200 = GetDunningTimingResponse200.from_dict(response.json())

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
) -> Response[Error | GetDunningTimingResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[Error | GetDunningTimingResponse200]:
    """Best-time-to-retry insights

     Historical retry success rate by hour-of-day (0-23) and day-of-week (0-6, Sunday=0), in UTC, plus
    the best-performing hour and day among buckets with enough samples. Read-only; does not change the
    live retry bandit. Cached for up to 5 minutes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetDunningTimingResponse200]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> Error | GetDunningTimingResponse200 | None:
    """Best-time-to-retry insights

     Historical retry success rate by hour-of-day (0-23) and day-of-week (0-6, Sunday=0), in UTC, plus
    the best-performing hour and day among buckets with enough samples. Read-only; does not change the
    live retry bandit. Cached for up to 5 minutes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetDunningTimingResponse200
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[Error | GetDunningTimingResponse200]:
    """Best-time-to-retry insights

     Historical retry success rate by hour-of-day (0-23) and day-of-week (0-6, Sunday=0), in UTC, plus
    the best-performing hour and day among buckets with enough samples. Read-only; does not change the
    live retry bandit. Cached for up to 5 minutes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetDunningTimingResponse200]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> Error | GetDunningTimingResponse200 | None:
    """Best-time-to-retry insights

     Historical retry success rate by hour-of-day (0-23) and day-of-week (0-6, Sunday=0), in UTC, plus
    the best-performing hour and day among buckets with enough samples. Read-only; does not change the
    live retry bandit. Cached for up to 5 minutes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetDunningTimingResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
