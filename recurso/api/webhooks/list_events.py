from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.list_events_response_200 import ListEventsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    type_: str | Unset = UNSET,
    object_id: UUID | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["type"] = type_

    json_object_id: str | Unset = UNSET
    if not isinstance(object_id, Unset):
        json_object_id = str(object_id)
    params["object_id"] = json_object_id

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/events",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | ListEventsResponse200 | None:
    if response.status_code == 200:
        response_200 = ListEventsResponse200.from_dict(response.json())

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
) -> Response[Error | ListEventsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    type_: str | Unset = UNSET,
    object_id: UUID | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = UNSET,
) -> Response[Error | ListEventsResponse200]:
    """List events

     Chronological feed of billing events emitted for this tenant.

    Args:
        type_ (str | Unset):
        object_id (UUID | Unset):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListEventsResponse200]
    """

    kwargs = _get_kwargs(
        type_=type_,
        object_id=object_id,
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
    type_: str | Unset = UNSET,
    object_id: UUID | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = UNSET,
) -> Error | ListEventsResponse200 | None:
    """List events

     Chronological feed of billing events emitted for this tenant.

    Args:
        type_ (str | Unset):
        object_id (UUID | Unset):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListEventsResponse200
    """

    return sync_detailed(
        client=client,
        type_=type_,
        object_id=object_id,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    type_: str | Unset = UNSET,
    object_id: UUID | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = UNSET,
) -> Response[Error | ListEventsResponse200]:
    """List events

     Chronological feed of billing events emitted for this tenant.

    Args:
        type_ (str | Unset):
        object_id (UUID | Unset):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListEventsResponse200]
    """

    kwargs = _get_kwargs(
        type_=type_,
        object_id=object_id,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    type_: str | Unset = UNSET,
    object_id: UUID | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = UNSET,
) -> Error | ListEventsResponse200 | None:
    """List events

     Chronological feed of billing events emitted for this tenant.

    Args:
        type_ (str | Unset):
        object_id (UUID | Unset):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListEventsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            type_=type_,
            object_id=object_id,
            limit=limit,
            offset=offset,
        )
    ).parsed
