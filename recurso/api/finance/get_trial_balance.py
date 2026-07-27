from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.get_trial_balance_response_200 import GetTrialBalanceResponse200
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    *,
    entity_id: UUID | Unset = UNSET,
    consolidated: bool | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_entity_id: str | Unset = UNSET
    if not isinstance(entity_id, Unset):
        json_entity_id = str(entity_id)
    params["entity_id"] = json_entity_id

    params["consolidated"] = consolidated


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/ledger/trial-balance",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | GetTrialBalanceResponse200 | None:
    if response.status_code == 200:
        response_200 = GetTrialBalanceResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | GetTrialBalanceResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    entity_id: UUID | Unset = UNSET,
    consolidated: bool | Unset = UNSET,

) -> Response[Error | GetTrialBalanceResponse200]:
    """ Trial balance

     Every account with its posted debit/credit totals, its balance on the
    account's normal side, an abnormal-sign flag, and the double-entry
    invariant (total debits == total credits). Read-only. Each line is
    tagged with its legal entity (Multi-Entity Books); pass `entity_id` to
    scope to one entity, or `consolidated=true` to roll every entity's
    accounts up by code into one tenant-wide view.

    Args:
        entity_id (UUID | Unset):
        consolidated (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetTrialBalanceResponse200]
     """


    kwargs = _get_kwargs(
        entity_id=entity_id,
consolidated=consolidated,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    entity_id: UUID | Unset = UNSET,
    consolidated: bool | Unset = UNSET,

) -> Error | GetTrialBalanceResponse200 | None:
    """ Trial balance

     Every account with its posted debit/credit totals, its balance on the
    account's normal side, an abnormal-sign flag, and the double-entry
    invariant (total debits == total credits). Read-only. Each line is
    tagged with its legal entity (Multi-Entity Books); pass `entity_id` to
    scope to one entity, or `consolidated=true` to roll every entity's
    accounts up by code into one tenant-wide view.

    Args:
        entity_id (UUID | Unset):
        consolidated (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetTrialBalanceResponse200
     """


    return sync_detailed(
        client=client,
entity_id=entity_id,
consolidated=consolidated,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    entity_id: UUID | Unset = UNSET,
    consolidated: bool | Unset = UNSET,

) -> Response[Error | GetTrialBalanceResponse200]:
    """ Trial balance

     Every account with its posted debit/credit totals, its balance on the
    account's normal side, an abnormal-sign flag, and the double-entry
    invariant (total debits == total credits). Read-only. Each line is
    tagged with its legal entity (Multi-Entity Books); pass `entity_id` to
    scope to one entity, or `consolidated=true` to roll every entity's
    accounts up by code into one tenant-wide view.

    Args:
        entity_id (UUID | Unset):
        consolidated (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetTrialBalanceResponse200]
     """


    kwargs = _get_kwargs(
        entity_id=entity_id,
consolidated=consolidated,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    entity_id: UUID | Unset = UNSET,
    consolidated: bool | Unset = UNSET,

) -> Error | GetTrialBalanceResponse200 | None:
    """ Trial balance

     Every account with its posted debit/credit totals, its balance on the
    account's normal side, an abnormal-sign flag, and the double-entry
    invariant (total debits == total credits). Read-only. Each line is
    tagged with its legal entity (Multi-Entity Books); pass `entity_id` to
    scope to one entity, or `consolidated=true` to roll every entity's
    accounts up by code into one tenant-wide view.

    Args:
        entity_id (UUID | Unset):
        consolidated (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetTrialBalanceResponse200
     """


    return (await asyncio_detailed(
        client=client,
entity_id=entity_id,
consolidated=consolidated,

    )).parsed
