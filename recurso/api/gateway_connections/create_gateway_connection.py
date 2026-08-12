from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_gateway_connection_body import CreateGatewayConnectionBody
from ...models.create_gateway_connection_response_201 import CreateGatewayConnectionResponse201
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    *,
    body: CreateGatewayConnectionBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/gateway-connections",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | CreateGatewayConnectionResponse201 | Error | None:
    if response.status_code == 201:
        response_201 = CreateGatewayConnectionResponse201.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403

    if response.status_code == 503:
        response_503 = cast(Any, None)
        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | CreateGatewayConnectionResponse201 | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateGatewayConnectionBody,
) -> Response[Any | CreateGatewayConnectionResponse201 | Error]:
    """Connect (or replace) a payment gateway

     Stores the tenant's own gateway credentials, sealed at rest. Secrets are
    write-only and never returned. Replaces any existing active connection
    for the provider. Owner/admin only.

    Args:
        body (CreateGatewayConnectionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateGatewayConnectionResponse201 | Error]
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
    body: CreateGatewayConnectionBody,
) -> Any | CreateGatewayConnectionResponse201 | Error | None:
    """Connect (or replace) a payment gateway

     Stores the tenant's own gateway credentials, sealed at rest. Secrets are
    write-only and never returned. Replaces any existing active connection
    for the provider. Owner/admin only.

    Args:
        body (CreateGatewayConnectionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateGatewayConnectionResponse201 | Error
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateGatewayConnectionBody,
) -> Response[Any | CreateGatewayConnectionResponse201 | Error]:
    """Connect (or replace) a payment gateway

     Stores the tenant's own gateway credentials, sealed at rest. Secrets are
    write-only and never returned. Replaces any existing active connection
    for the provider. Owner/admin only.

    Args:
        body (CreateGatewayConnectionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateGatewayConnectionResponse201 | Error]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateGatewayConnectionBody,
) -> Any | CreateGatewayConnectionResponse201 | Error | None:
    """Connect (or replace) a payment gateway

     Stores the tenant's own gateway credentials, sealed at rest. Secrets are
    write-only and never returned. Replaces any existing active connection
    for the provider. Owner/admin only.

    Args:
        body (CreateGatewayConnectionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateGatewayConnectionResponse201 | Error
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
