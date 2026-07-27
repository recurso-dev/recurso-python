from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.retry_eue_invoice_response_200 import RetryEUEInvoiceResponse200
from typing import cast
from uuid import UUID



def _get_kwargs(
    id: UUID,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/invoices/{id}/eu-einvoice/retry".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | RetryEUEInvoiceResponse200 | None:
    if response.status_code == 200:
        response_200 = RetryEUEInvoiceResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | RetryEUEInvoiceResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Error | RetryEUEInvoiceResponse200]:
    """ Regenerate and re-transmit the EU e-invoice

     Re-runs EN 16931 UBL generation and Access Point transmission for the invoice, recovering a
    generation or transmission failure. Idempotent. data:null when the tenant hasn't opted in.

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | RetryEUEInvoiceResponse200]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> Error | RetryEUEInvoiceResponse200 | None:
    """ Regenerate and re-transmit the EU e-invoice

     Re-runs EN 16931 UBL generation and Access Point transmission for the invoice, recovering a
    generation or transmission failure. Idempotent. data:null when the tenant hasn't opted in.

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | RetryEUEInvoiceResponse200
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Error | RetryEUEInvoiceResponse200]:
    """ Regenerate and re-transmit the EU e-invoice

     Re-runs EN 16931 UBL generation and Access Point transmission for the invoice, recovering a
    generation or transmission failure. Idempotent. data:null when the tenant hasn't opted in.

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | RetryEUEInvoiceResponse200]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> Error | RetryEUEInvoiceResponse200 | None:
    """ Regenerate and re-transmit the EU e-invoice

     Re-runs EN 16931 UBL generation and Access Point transmission for the invoice, recovering a
    generation or transmission failure. Idempotent. data:null when the tenant hasn't opted in.

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | RetryEUEInvoiceResponse200
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
