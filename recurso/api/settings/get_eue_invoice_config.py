from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.get_eue_invoice_config_response_200 import GetEUEInvoiceConfigResponse200
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    *,
    entity_id: UUID | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_entity_id: str | Unset = UNSET
    if not isinstance(entity_id, Unset):
        json_entity_id = str(entity_id)
    params["entity_id"] = json_entity_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/settings/eu-einvoice",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | GetEUEInvoiceConfigResponse200 | None:
    if response.status_code == 200:
        response_200 = GetEUEInvoiceConfigResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | GetEUEInvoiceConfigResponse200]:
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

) -> Response[Error | GetEUEInvoiceConfigResponse200]:
    """ Get EU e-invoicing configuration

     Returns the tenant's EU e-invoicing config (opt-in flag + EN 16931 seller identity), or an empty
    disabled default when none is set.

    Args:
        entity_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetEUEInvoiceConfigResponse200]
     """


    kwargs = _get_kwargs(
        entity_id=entity_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    entity_id: UUID | Unset = UNSET,

) -> Error | GetEUEInvoiceConfigResponse200 | None:
    """ Get EU e-invoicing configuration

     Returns the tenant's EU e-invoicing config (opt-in flag + EN 16931 seller identity), or an empty
    disabled default when none is set.

    Args:
        entity_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetEUEInvoiceConfigResponse200
     """


    return sync_detailed(
        client=client,
entity_id=entity_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    entity_id: UUID | Unset = UNSET,

) -> Response[Error | GetEUEInvoiceConfigResponse200]:
    """ Get EU e-invoicing configuration

     Returns the tenant's EU e-invoicing config (opt-in flag + EN 16931 seller identity), or an empty
    disabled default when none is set.

    Args:
        entity_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetEUEInvoiceConfigResponse200]
     """


    kwargs = _get_kwargs(
        entity_id=entity_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    entity_id: UUID | Unset = UNSET,

) -> Error | GetEUEInvoiceConfigResponse200 | None:
    """ Get EU e-invoicing configuration

     Returns the tenant's EU e-invoicing config (opt-in flag + EN 16931 seller identity), or an empty
    disabled default when none is set.

    Args:
        entity_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetEUEInvoiceConfigResponse200
     """


    return (await asyncio_detailed(
        client=client,
entity_id=entity_id,

    )).parsed
