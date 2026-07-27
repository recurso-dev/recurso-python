from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.put_v1_gateway_connections_provider_webhook_secret_body import PutV1GatewayConnectionsProviderWebhookSecretBody
from ...models.put_v1_gateway_connections_provider_webhook_secret_provider import PutV1GatewayConnectionsProviderWebhookSecretProvider
from typing import cast



def _get_kwargs(
    provider: PutV1GatewayConnectionsProviderWebhookSecretProvider,
    *,
    body: PutV1GatewayConnectionsProviderWebhookSecretBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/gateway-connections/{provider}/webhook-secret".format(provider=quote(str(provider), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
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

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())



        return response_404

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
    provider: PutV1GatewayConnectionsProviderWebhookSecretProvider,
    *,
    client: AuthenticatedClient | Client,
    body: PutV1GatewayConnectionsProviderWebhookSecretBody,

) -> Response[Any | Error]:
    """ Set the webhook signing secret on the active connection

     Updates the webhook secret in place (id unchanged, so the per-connection
    webhook URL stays stable). Two-step connect: create the webhook in the
    gateway console using the per-connection URL, then paste the secret here.
    Owner/admin only.

    Args:
        provider (PutV1GatewayConnectionsProviderWebhookSecretProvider):
        body (PutV1GatewayConnectionsProviderWebhookSecretBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
     """


    kwargs = _get_kwargs(
        provider=provider,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    provider: PutV1GatewayConnectionsProviderWebhookSecretProvider,
    *,
    client: AuthenticatedClient | Client,
    body: PutV1GatewayConnectionsProviderWebhookSecretBody,

) -> Any | Error | None:
    """ Set the webhook signing secret on the active connection

     Updates the webhook secret in place (id unchanged, so the per-connection
    webhook URL stays stable). Two-step connect: create the webhook in the
    gateway console using the per-connection URL, then paste the secret here.
    Owner/admin only.

    Args:
        provider (PutV1GatewayConnectionsProviderWebhookSecretProvider):
        body (PutV1GatewayConnectionsProviderWebhookSecretBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
     """


    return sync_detailed(
        provider=provider,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    provider: PutV1GatewayConnectionsProviderWebhookSecretProvider,
    *,
    client: AuthenticatedClient | Client,
    body: PutV1GatewayConnectionsProviderWebhookSecretBody,

) -> Response[Any | Error]:
    """ Set the webhook signing secret on the active connection

     Updates the webhook secret in place (id unchanged, so the per-connection
    webhook URL stays stable). Two-step connect: create the webhook in the
    gateway console using the per-connection URL, then paste the secret here.
    Owner/admin only.

    Args:
        provider (PutV1GatewayConnectionsProviderWebhookSecretProvider):
        body (PutV1GatewayConnectionsProviderWebhookSecretBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
     """


    kwargs = _get_kwargs(
        provider=provider,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    provider: PutV1GatewayConnectionsProviderWebhookSecretProvider,
    *,
    client: AuthenticatedClient | Client,
    body: PutV1GatewayConnectionsProviderWebhookSecretBody,

) -> Any | Error | None:
    """ Set the webhook signing secret on the active connection

     Updates the webhook secret in place (id unchanged, so the per-connection
    webhook URL stays stable). Two-step connect: create the webhook in the
    gateway console using the per-connection URL, then paste the secret here.
    Owner/admin only.

    Args:
        provider (PutV1GatewayConnectionsProviderWebhookSecretProvider):
        body (PutV1GatewayConnectionsProviderWebhookSecretBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
     """


    return (await asyncio_detailed(
        provider=provider,
client=client,
body=body,

    )).parsed
