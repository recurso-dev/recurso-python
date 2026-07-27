from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.trigger_accounting_sync_response_200 import TriggerAccountingSyncResponse200
from ...models.trigger_accounting_sync_response_202 import TriggerAccountingSyncResponse202
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/accounting/sync",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | TriggerAccountingSyncResponse200 | TriggerAccountingSyncResponse202 | None:
    if response.status_code == 200:
        response_200 = TriggerAccountingSyncResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = TriggerAccountingSyncResponse202.from_dict(response.json())

        return response_202

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | TriggerAccountingSyncResponse200 | TriggerAccountingSyncResponse202]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[Error | TriggerAccountingSyncResponse200 | TriggerAccountingSyncResponse202]:
    """Trigger a sync to connected accounting systems

     Starts a forced full re-push to every active accounting connection in
    the background and returns immediately — the sweep can take minutes
    for large tenants. Progress is observable via the sync-activity log
    and each connection's sync_status. One manual sync runs per tenant at
    a time; a request while one is running returns 200 with
    status=sync_already_running.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | TriggerAccountingSyncResponse200 | TriggerAccountingSyncResponse202]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> Error | TriggerAccountingSyncResponse200 | TriggerAccountingSyncResponse202 | None:
    """Trigger a sync to connected accounting systems

     Starts a forced full re-push to every active accounting connection in
    the background and returns immediately — the sweep can take minutes
    for large tenants. Progress is observable via the sync-activity log
    and each connection's sync_status. One manual sync runs per tenant at
    a time; a request while one is running returns 200 with
    status=sync_already_running.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | TriggerAccountingSyncResponse200 | TriggerAccountingSyncResponse202
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[Error | TriggerAccountingSyncResponse200 | TriggerAccountingSyncResponse202]:
    """Trigger a sync to connected accounting systems

     Starts a forced full re-push to every active accounting connection in
    the background and returns immediately — the sweep can take minutes
    for large tenants. Progress is observable via the sync-activity log
    and each connection's sync_status. One manual sync runs per tenant at
    a time; a request while one is running returns 200 with
    status=sync_already_running.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | TriggerAccountingSyncResponse200 | TriggerAccountingSyncResponse202]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> Error | TriggerAccountingSyncResponse200 | TriggerAccountingSyncResponse202 | None:
    """Trigger a sync to connected accounting systems

     Starts a forced full re-push to every active accounting connection in
    the background and returns immediately — the sweep can take minutes
    for large tenants. Progress is observable via the sync-activity log
    and each connection's sync_status. One manual sync runs per tenant at
    a time; a request while one is running returns 200 with
    status=sync_already_running.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | TriggerAccountingSyncResponse200 | TriggerAccountingSyncResponse202
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
