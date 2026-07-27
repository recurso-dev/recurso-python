from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.mcp_settings import MCPSettings
from ...models.update_mcp_settings_response_200 import UpdateMCPSettingsResponse200
from typing import cast



def _get_kwargs(
    *,
    body: MCPSettings,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/settings/mcp",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | UpdateMCPSettingsResponse200 | None:
    if response.status_code == 200:
        response_200 = UpdateMCPSettingsResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | UpdateMCPSettingsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: MCPSettings,

) -> Response[Error | UpdateMCPSettingsResponse200]:
    """ Update MCP server settings

     Upserts the tenant's MCP opt-in. Enabling `tier3_enabled` lets AI agents run money-path /
    destructive MCP tools (convert quote to invoice, cancel subscription, issue credit note, top up
    wallet, …) against this tenant.

    Args:
        body (MCPSettings): A tenant's MCP server opt-in.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | UpdateMCPSettingsResponse200]
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
    body: MCPSettings,

) -> Error | UpdateMCPSettingsResponse200 | None:
    """ Update MCP server settings

     Upserts the tenant's MCP opt-in. Enabling `tier3_enabled` lets AI agents run money-path /
    destructive MCP tools (convert quote to invoice, cancel subscription, issue credit note, top up
    wallet, …) against this tenant.

    Args:
        body (MCPSettings): A tenant's MCP server opt-in.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | UpdateMCPSettingsResponse200
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: MCPSettings,

) -> Response[Error | UpdateMCPSettingsResponse200]:
    """ Update MCP server settings

     Upserts the tenant's MCP opt-in. Enabling `tier3_enabled` lets AI agents run money-path /
    destructive MCP tools (convert quote to invoice, cancel subscription, issue credit note, top up
    wallet, …) against this tenant.

    Args:
        body (MCPSettings): A tenant's MCP server opt-in.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | UpdateMCPSettingsResponse200]
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
    body: MCPSettings,

) -> Error | UpdateMCPSettingsResponse200 | None:
    """ Update MCP server settings

     Upserts the tenant's MCP opt-in. Enabling `tier3_enabled` lets AI agents run money-path /
    destructive MCP tools (convert quote to invoice, cancel subscription, issue credit note, top up
    wallet, …) against this tenant.

    Args:
        body (MCPSettings): A tenant's MCP server opt-in.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | UpdateMCPSettingsResponse200
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
