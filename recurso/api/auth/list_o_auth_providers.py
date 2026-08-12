from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_o_auth_providers_response_200 import ListOAuthProvidersResponse200
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/auth/oauth/providers",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ListOAuthProvidersResponse200 | None:
    if response.status_code == 200:
        response_200 = ListOAuthProvidersResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ListOAuthProvidersResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[ListOAuthProvidersResponse200]:
    """List social-login providers and whether each is enabled

     Returns every provider this build understands with an `enabled` flag. A provider is enabled only
    when its client id AND secret env vars are set (GOOGLE_CLIENT_ID/GOOGLE_CLIENT_SECRET,
    GITHUB_CLIENT_ID/GITHUB_CLIENT_SECRET). The dashboard uses this to show/hide the social buttons.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListOAuthProvidersResponse200]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> ListOAuthProvidersResponse200 | None:
    """List social-login providers and whether each is enabled

     Returns every provider this build understands with an `enabled` flag. A provider is enabled only
    when its client id AND secret env vars are set (GOOGLE_CLIENT_ID/GOOGLE_CLIENT_SECRET,
    GITHUB_CLIENT_ID/GITHUB_CLIENT_SECRET). The dashboard uses this to show/hide the social buttons.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListOAuthProvidersResponse200
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[ListOAuthProvidersResponse200]:
    """List social-login providers and whether each is enabled

     Returns every provider this build understands with an `enabled` flag. A provider is enabled only
    when its client id AND secret env vars are set (GOOGLE_CLIENT_ID/GOOGLE_CLIENT_SECRET,
    GITHUB_CLIENT_ID/GITHUB_CLIENT_SECRET). The dashboard uses this to show/hide the social buttons.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListOAuthProvidersResponse200]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> ListOAuthProvidersResponse200 | None:
    """List social-login providers and whether each is enabled

     Returns every provider this build understands with an `enabled` flag. A provider is enabled only
    when its client id AND secret env vars are set (GOOGLE_CLIENT_ID/GOOGLE_CLIENT_SECRET,
    GITHUB_CLIENT_ID/GITHUB_CLIENT_SECRET). The dashboard uses this to show/hide the social buttons.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListOAuthProvidersResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
