from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.get_collections_queue_managed_by import GetCollectionsQueueManagedBy
from ...models.get_collections_queue_response_200 import GetCollectionsQueueResponse200
from ...models.get_collections_queue_status import GetCollectionsQueueStatus
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    status: GetCollectionsQueueStatus | Unset = UNSET,
    managed_by: GetCollectionsQueueManagedBy | Unset = UNSET,
    page: int | Unset = 1,
    per_page: int | Unset = 50,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    json_managed_by: str | Unset = UNSET
    if not isinstance(managed_by, Unset):
        json_managed_by = managed_by.value

    params["managed_by"] = json_managed_by

    params["page"] = page

    params["per_page"] = per_page


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/collections/queue",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | GetCollectionsQueueResponse200 | None:
    if response.status_code == 200:
        response_200 = GetCollectionsQueueResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | GetCollectionsQueueResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    status: GetCollectionsQueueStatus | Unset = UNSET,
    managed_by: GetCollectionsQueueManagedBy | Unset = UNSET,
    page: int | Unset = 1,
    per_page: int | Unset = 50,

) -> Response[Error | GetCollectionsQueueResponse200]:
    """ Collections worklist of currently-failing invoices

     Operator-facing list of invoices in a recovery state (past_due or uncollectible with a balance
    owing), each with its customer, amount remaining, days overdue, retry count, last failure code, next
    scheduled retry, which engine owns it, and the latest ACH attempt status. Read-only.

    Args:
        status (GetCollectionsQueueStatus | Unset):
        managed_by (GetCollectionsQueueManagedBy | Unset):
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetCollectionsQueueResponse200]
     """


    kwargs = _get_kwargs(
        status=status,
managed_by=managed_by,
page=page,
per_page=per_page,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    status: GetCollectionsQueueStatus | Unset = UNSET,
    managed_by: GetCollectionsQueueManagedBy | Unset = UNSET,
    page: int | Unset = 1,
    per_page: int | Unset = 50,

) -> Error | GetCollectionsQueueResponse200 | None:
    """ Collections worklist of currently-failing invoices

     Operator-facing list of invoices in a recovery state (past_due or uncollectible with a balance
    owing), each with its customer, amount remaining, days overdue, retry count, last failure code, next
    scheduled retry, which engine owns it, and the latest ACH attempt status. Read-only.

    Args:
        status (GetCollectionsQueueStatus | Unset):
        managed_by (GetCollectionsQueueManagedBy | Unset):
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetCollectionsQueueResponse200
     """


    return sync_detailed(
        client=client,
status=status,
managed_by=managed_by,
page=page,
per_page=per_page,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    status: GetCollectionsQueueStatus | Unset = UNSET,
    managed_by: GetCollectionsQueueManagedBy | Unset = UNSET,
    page: int | Unset = 1,
    per_page: int | Unset = 50,

) -> Response[Error | GetCollectionsQueueResponse200]:
    """ Collections worklist of currently-failing invoices

     Operator-facing list of invoices in a recovery state (past_due or uncollectible with a balance
    owing), each with its customer, amount remaining, days overdue, retry count, last failure code, next
    scheduled retry, which engine owns it, and the latest ACH attempt status. Read-only.

    Args:
        status (GetCollectionsQueueStatus | Unset):
        managed_by (GetCollectionsQueueManagedBy | Unset):
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetCollectionsQueueResponse200]
     """


    kwargs = _get_kwargs(
        status=status,
managed_by=managed_by,
page=page,
per_page=per_page,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    status: GetCollectionsQueueStatus | Unset = UNSET,
    managed_by: GetCollectionsQueueManagedBy | Unset = UNSET,
    page: int | Unset = 1,
    per_page: int | Unset = 50,

) -> Error | GetCollectionsQueueResponse200 | None:
    """ Collections worklist of currently-failing invoices

     Operator-facing list of invoices in a recovery state (past_due or uncollectible with a balance
    owing), each with its customer, amount remaining, days overdue, retry count, last failure code, next
    scheduled retry, which engine owns it, and the latest ACH attempt status. Read-only.

    Args:
        status (GetCollectionsQueueStatus | Unset):
        managed_by (GetCollectionsQueueManagedBy | Unset):
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetCollectionsQueueResponse200
     """


    return (await asyncio_detailed(
        client=client,
status=status,
managed_by=managed_by,
page=page,
per_page=per_page,

    )).parsed
