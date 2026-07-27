from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.simulate_charges_body import SimulateChargesBody
from ...models.simulate_charges_response_200 import SimulateChargesResponse200
from typing import cast
from uuid import UUID



def _get_kwargs(
    id: UUID,
    *,
    body: SimulateChargesBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/plans/{id}/simulate-charges".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | SimulateChargesResponse200 | None:
    if response.status_code == 200:
        response_200 = SimulateChargesResponse200.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | SimulateChargesResponse200]:
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
    body: SimulateChargesBody,

) -> Response[Error | SimulateChargesResponse200]:
    """ Simulate a proposed charge set (read-only)

     Rates a PROPOSED charge set against sample usage and returns the rated lines, the subtotal, and a
    balanced general-ledger preview (DR Accounts Receivable / CR Revenue). Pre-tax — GST/tax is resolved
    at invoice time. Nothing is persisted and no ledger legs are posted. Sample usage comes from `usage`
    (per metric_id); metrics without an explicit entry fall back to `subscription_id`'s current-period
    usage when given.

    Args:
        id (UUID):
        body (SimulateChargesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SimulateChargesResponse200]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: SimulateChargesBody,

) -> Error | SimulateChargesResponse200 | None:
    """ Simulate a proposed charge set (read-only)

     Rates a PROPOSED charge set against sample usage and returns the rated lines, the subtotal, and a
    balanced general-ledger preview (DR Accounts Receivable / CR Revenue). Pre-tax — GST/tax is resolved
    at invoice time. Nothing is persisted and no ledger legs are posted. Sample usage comes from `usage`
    (per metric_id); metrics without an explicit entry fall back to `subscription_id`'s current-period
    usage when given.

    Args:
        id (UUID):
        body (SimulateChargesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SimulateChargesResponse200
     """


    return sync_detailed(
        id=id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: SimulateChargesBody,

) -> Response[Error | SimulateChargesResponse200]:
    """ Simulate a proposed charge set (read-only)

     Rates a PROPOSED charge set against sample usage and returns the rated lines, the subtotal, and a
    balanced general-ledger preview (DR Accounts Receivable / CR Revenue). Pre-tax — GST/tax is resolved
    at invoice time. Nothing is persisted and no ledger legs are posted. Sample usage comes from `usage`
    (per metric_id); metrics without an explicit entry fall back to `subscription_id`'s current-period
    usage when given.

    Args:
        id (UUID):
        body (SimulateChargesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SimulateChargesResponse200]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: SimulateChargesBody,

) -> Error | SimulateChargesResponse200 | None:
    """ Simulate a proposed charge set (read-only)

     Rates a PROPOSED charge set against sample usage and returns the rated lines, the subtotal, and a
    balanced general-ledger preview (DR Accounts Receivable / CR Revenue). Pre-tax — GST/tax is resolved
    at invoice time. Nothing is persisted and no ledger legs are posted. Sample usage comes from `usage`
    (per metric_id); metrics without an explicit entry fall back to `subscription_id`'s current-period
    usage when given.

    Args:
        id (UUID):
        body (SimulateChargesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SimulateChargesResponse200
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
