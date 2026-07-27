from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.get_close_pack_response_200 import GetClosePackResponse200
from ...types import UNSET, Response


def _get_kwargs(
    *,
    month: int,
    year: int,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["month"] = month

    params["year"] = year

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/finance/close-pack",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | GetClosePackResponse200 | None:
    if response.status_code == 200:
        response_200 = GetClosePackResponse200.from_dict(response.json())

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
) -> Response[Error | GetClosePackResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    month: int,
    year: int,
) -> Response[Error | GetClosePackResponse200]:
    """Month-end close pack

     One read-only artifact for a calendar month: the trial balance, an
    on-demand reconciliation report, the Deferred Revenue rollforward (with
    the schedule-sourced recognition view when rev-rec is wired), a pointer
    to the GL CSV export, and a `ready_to_close` verdict. The period is
    ready to close when the trial balance is in balance and reconciliation
    finds zero discrepancies; otherwise `blockers` lists why. Nothing is
    persisted — closing the period stays a human decision.

    Args:
        month (int):
        year (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetClosePackResponse200]
    """

    kwargs = _get_kwargs(
        month=month,
        year=year,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    month: int,
    year: int,
) -> Error | GetClosePackResponse200 | None:
    """Month-end close pack

     One read-only artifact for a calendar month: the trial balance, an
    on-demand reconciliation report, the Deferred Revenue rollforward (with
    the schedule-sourced recognition view when rev-rec is wired), a pointer
    to the GL CSV export, and a `ready_to_close` verdict. The period is
    ready to close when the trial balance is in balance and reconciliation
    finds zero discrepancies; otherwise `blockers` lists why. Nothing is
    persisted — closing the period stays a human decision.

    Args:
        month (int):
        year (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetClosePackResponse200
    """

    return sync_detailed(
        client=client,
        month=month,
        year=year,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    month: int,
    year: int,
) -> Response[Error | GetClosePackResponse200]:
    """Month-end close pack

     One read-only artifact for a calendar month: the trial balance, an
    on-demand reconciliation report, the Deferred Revenue rollforward (with
    the schedule-sourced recognition view when rev-rec is wired), a pointer
    to the GL CSV export, and a `ready_to_close` verdict. The period is
    ready to close when the trial balance is in balance and reconciliation
    finds zero discrepancies; otherwise `blockers` lists why. Nothing is
    persisted — closing the period stays a human decision.

    Args:
        month (int):
        year (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetClosePackResponse200]
    """

    kwargs = _get_kwargs(
        month=month,
        year=year,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    month: int,
    year: int,
) -> Error | GetClosePackResponse200 | None:
    """Month-end close pack

     One read-only artifact for a calendar month: the trial balance, an
    on-demand reconciliation report, the Deferred Revenue rollforward (with
    the schedule-sourced recognition view when rev-rec is wired), a pointer
    to the GL CSV export, and a `ready_to_close` verdict. The period is
    ready to close when the trial balance is in balance and reconciliation
    finds zero discrepancies; otherwise `blockers` lists why. Nothing is
    persisted — closing the period stays a human decision.

    Args:
        month (int):
        year (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetClosePackResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            month=month,
            year=year,
        )
    ).parsed
