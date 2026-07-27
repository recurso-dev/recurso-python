from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.set_tax_registrations_body import SetTaxRegistrationsBody
from ...models.set_tax_registrations_response_200 import SetTaxRegistrationsResponse200
from typing import cast



def _get_kwargs(
    *,
    body: SetTaxRegistrationsBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/settings/tax/registrations",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | SetTaxRegistrationsResponse200 | None:
    if response.status_code == 200:
        response_200 = SetTaxRegistrationsResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())



        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | SetTaxRegistrationsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SetTaxRegistrationsBody,

) -> Response[Error | SetTaxRegistrationsResponse200]:
    """ Set US sales-tax registrations

     Replaces the tenant's entire registration set. Owner/admin only.

    Args:
        body (SetTaxRegistrationsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SetTaxRegistrationsResponse200]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: SetTaxRegistrationsBody,

) -> Error | SetTaxRegistrationsResponse200 | None:
    """ Set US sales-tax registrations

     Replaces the tenant's entire registration set. Owner/admin only.

    Args:
        body (SetTaxRegistrationsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SetTaxRegistrationsResponse200
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SetTaxRegistrationsBody,

) -> Response[Error | SetTaxRegistrationsResponse200]:
    """ Set US sales-tax registrations

     Replaces the tenant's entire registration set. Owner/admin only.

    Args:
        body (SetTaxRegistrationsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SetTaxRegistrationsResponse200]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SetTaxRegistrationsBody,

) -> Error | SetTaxRegistrationsResponse200 | None:
    """ Set US sales-tax registrations

     Replaces the tenant's entire registration set. Owner/admin only.

    Args:
        body (SetTaxRegistrationsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SetTaxRegistrationsResponse200
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
