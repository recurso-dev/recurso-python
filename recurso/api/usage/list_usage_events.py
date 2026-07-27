from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    *,
    customer_id: UUID | Unset = UNSET,
    dimension: str | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_customer_id: str | Unset = UNSET
    if not isinstance(customer_id, Unset):
        json_customer_id = str(customer_id)
    params["customer_id"] = json_customer_id

    params["dimension"] = dimension

    params["limit"] = limit

    params["offset"] = offset


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/usage/events",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Error | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    customer_id: UUID | Unset = UNSET,
    dimension: str | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,

) -> Response[Any | Error]:
    r""" List recent raw usage events

     Newest-first raw ingestion stream for debugging metering — \"did my events actually land?\".
    Optional customer_id and dimension filters; limit (max 200, default 50) and offset paging.

    Args:
        customer_id (UUID | Unset):
        dimension (str | Unset):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
     """


    kwargs = _get_kwargs(
        customer_id=customer_id,
dimension=dimension,
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
    customer_id: UUID | Unset = UNSET,
    dimension: str | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,

) -> Any | Error | None:
    r""" List recent raw usage events

     Newest-first raw ingestion stream for debugging metering — \"did my events actually land?\".
    Optional customer_id and dimension filters; limit (max 200, default 50) and offset paging.

    Args:
        customer_id (UUID | Unset):
        dimension (str | Unset):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
     """


    return sync_detailed(
        client=client,
customer_id=customer_id,
dimension=dimension,
limit=limit,
offset=offset,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    customer_id: UUID | Unset = UNSET,
    dimension: str | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,

) -> Response[Any | Error]:
    r""" List recent raw usage events

     Newest-first raw ingestion stream for debugging metering — \"did my events actually land?\".
    Optional customer_id and dimension filters; limit (max 200, default 50) and offset paging.

    Args:
        customer_id (UUID | Unset):
        dimension (str | Unset):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
     """


    kwargs = _get_kwargs(
        customer_id=customer_id,
dimension=dimension,
limit=limit,
offset=offset,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    customer_id: UUID | Unset = UNSET,
    dimension: str | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,

) -> Any | Error | None:
    r""" List recent raw usage events

     Newest-first raw ingestion stream for debugging metering — \"did my events actually land?\".
    Optional customer_id and dimension filters; limit (max 200, default 50) and offset paging.

    Args:
        customer_id (UUID | Unset):
        dimension (str | Unset):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
     """


    return (await asyncio_detailed(
        client=client,
customer_id=customer_id,
dimension=dimension,
limit=limit,
offset=offset,

    )).parsed
