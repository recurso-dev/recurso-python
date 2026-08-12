from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_integration_connection_category import DeleteIntegrationConnectionCategory
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    category: DeleteIntegrationConnectionCategory,
    provider: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/integration-connections/{category}/{provider}".format(
            category=quote(str(category), safe=""),
            provider=quote(str(provider), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Error | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

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
    category: DeleteIntegrationConnectionCategory,
    provider: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | Error]:
    """Disconnect a tax/CRM/storage integration

     Soft-disconnects the tenant's active connection. Owner/admin only.

    Args:
        category (DeleteIntegrationConnectionCategory):
        provider (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
    """

    kwargs = _get_kwargs(
        category=category,
        provider=provider,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    category: DeleteIntegrationConnectionCategory,
    provider: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | Error | None:
    """Disconnect a tax/CRM/storage integration

     Soft-disconnects the tenant's active connection. Owner/admin only.

    Args:
        category (DeleteIntegrationConnectionCategory):
        provider (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
    """

    return sync_detailed(
        category=category,
        provider=provider,
        client=client,
    ).parsed


async def asyncio_detailed(
    category: DeleteIntegrationConnectionCategory,
    provider: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | Error]:
    """Disconnect a tax/CRM/storage integration

     Soft-disconnects the tenant's active connection. Owner/admin only.

    Args:
        category (DeleteIntegrationConnectionCategory):
        provider (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
    """

    kwargs = _get_kwargs(
        category=category,
        provider=provider,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    category: DeleteIntegrationConnectionCategory,
    provider: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | Error | None:
    """Disconnect a tax/CRM/storage integration

     Soft-disconnects the tenant's active connection. Owner/admin only.

    Args:
        category (DeleteIntegrationConnectionCategory):
        provider (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
    """

    return (
        await asyncio_detailed(
            category=category,
            provider=provider,
            client=client,
        )
    ).parsed
