from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.get_mrr_by_entity_response_200 import GetMRRByEntityResponse200
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/analytics/mrr/by-entity",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | GetMRRByEntityResponse200 | None:
    if response.status_code == 200:
        response_200 = GetMRRByEntityResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | GetMRRByEntityResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[Error | GetMRRByEntityResponse200]:
    """ MRR broken down by legal entity

     MRR contribution of each legal entity (Multi-Entity Books), normalized to the reporting currency and
    sorted by MRR descending. Every entity appears (zero if it has no active MRR); a single-entity
    tenant gets one row. Cached for up to 5 minutes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetMRRByEntityResponse200]
     """


    kwargs = _get_kwargs(
        
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,

) -> Error | GetMRRByEntityResponse200 | None:
    """ MRR broken down by legal entity

     MRR contribution of each legal entity (Multi-Entity Books), normalized to the reporting currency and
    sorted by MRR descending. Every entity appears (zero if it has no active MRR); a single-entity
    tenant gets one row. Cached for up to 5 minutes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetMRRByEntityResponse200
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[Error | GetMRRByEntityResponse200]:
    """ MRR broken down by legal entity

     MRR contribution of each legal entity (Multi-Entity Books), normalized to the reporting currency and
    sorted by MRR descending. Every entity appears (zero if it has no active MRR); a single-entity
    tenant gets one row. Cached for up to 5 minutes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetMRRByEntityResponse200]
     """


    kwargs = _get_kwargs(
        
    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,

) -> Error | GetMRRByEntityResponse200 | None:
    """ MRR broken down by legal entity

     MRR contribution of each legal entity (Multi-Entity Books), normalized to the reporting currency and
    sorted by MRR descending. Every entity appears (zero if it has no active MRR); a single-entity
    tenant gets one row. Cached for up to 5 minutes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetMRRByEntityResponse200
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
