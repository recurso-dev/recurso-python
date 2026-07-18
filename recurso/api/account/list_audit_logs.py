import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.list_audit_logs_response_200 import ListAuditLogsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    entity_type: str | Unset = UNSET,
    entity_id: str | Unset = UNSET,
    actor: str | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["entity_type"] = entity_type

    params["entity_id"] = entity_id

    params["actor"] = actor

    json_from_: str | Unset = UNSET
    if not isinstance(from_, Unset):
        json_from_ = from_.isoformat()
    params["from"] = json_from_

    json_to: str | Unset = UNSET
    if not isinstance(to, Unset):
        json_to = to.isoformat()
    params["to"] = json_to

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/audit-logs",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | ListAuditLogsResponse200 | None:
    if response.status_code == 200:
        response_200 = ListAuditLogsResponse200.from_dict(response.json())

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
) -> Response[Error | ListAuditLogsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    entity_type: str | Unset = UNSET,
    entity_id: str | Unset = UNSET,
    actor: str | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
) -> Response[Error | ListAuditLogsResponse200]:
    """List the append-only audit trail

     Every successful config-grade mutation (plans, metrics, charges, coupons, webhooks, wallets, alerts,
    team, settings, ...) is recorded with actor, route, entity, and the request payload. The table is
    immutable: updates and deletes are rejected at the database level.

    Args:
        entity_type (str | Unset):
        entity_id (str | Unset):
        actor (str | Unset):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        limit (int | Unset):  Default: 100.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListAuditLogsResponse200]
    """

    kwargs = _get_kwargs(
        entity_type=entity_type,
        entity_id=entity_id,
        actor=actor,
        from_=from_,
        to=to,
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
    entity_type: str | Unset = UNSET,
    entity_id: str | Unset = UNSET,
    actor: str | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
) -> Error | ListAuditLogsResponse200 | None:
    """List the append-only audit trail

     Every successful config-grade mutation (plans, metrics, charges, coupons, webhooks, wallets, alerts,
    team, settings, ...) is recorded with actor, route, entity, and the request payload. The table is
    immutable: updates and deletes are rejected at the database level.

    Args:
        entity_type (str | Unset):
        entity_id (str | Unset):
        actor (str | Unset):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        limit (int | Unset):  Default: 100.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListAuditLogsResponse200
    """

    return sync_detailed(
        client=client,
        entity_type=entity_type,
        entity_id=entity_id,
        actor=actor,
        from_=from_,
        to=to,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    entity_type: str | Unset = UNSET,
    entity_id: str | Unset = UNSET,
    actor: str | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
) -> Response[Error | ListAuditLogsResponse200]:
    """List the append-only audit trail

     Every successful config-grade mutation (plans, metrics, charges, coupons, webhooks, wallets, alerts,
    team, settings, ...) is recorded with actor, route, entity, and the request payload. The table is
    immutable: updates and deletes are rejected at the database level.

    Args:
        entity_type (str | Unset):
        entity_id (str | Unset):
        actor (str | Unset):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        limit (int | Unset):  Default: 100.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListAuditLogsResponse200]
    """

    kwargs = _get_kwargs(
        entity_type=entity_type,
        entity_id=entity_id,
        actor=actor,
        from_=from_,
        to=to,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    entity_type: str | Unset = UNSET,
    entity_id: str | Unset = UNSET,
    actor: str | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
) -> Error | ListAuditLogsResponse200 | None:
    """List the append-only audit trail

     Every successful config-grade mutation (plans, metrics, charges, coupons, webhooks, wallets, alerts,
    team, settings, ...) is recorded with actor, route, entity, and the request payload. The table is
    immutable: updates and deletes are rejected at the database level.

    Args:
        entity_type (str | Unset):
        entity_id (str | Unset):
        actor (str | Unset):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        limit (int | Unset):  Default: 100.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListAuditLogsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            entity_type=entity_type,
            entity_id=entity_id,
            actor=actor,
            from_=from_,
            to=to,
            limit=limit,
            offset=offset,
        )
    ).parsed
