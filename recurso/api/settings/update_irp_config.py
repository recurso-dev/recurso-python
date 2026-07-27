from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.irp_config import IRPConfig
from ...models.update_irp_config_response_200 import UpdateIRPConfigResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: IRPConfig,
    entity_id: UUID | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_entity_id: str | Unset = UNSET
    if not isinstance(entity_id, Unset):
        json_entity_id = str(entity_id)
    params["entity_id"] = json_entity_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/settings/irp",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | UpdateIRPConfigResponse200 | None:
    if response.status_code == 200:
        response_200 = UpdateIRPConfigResponse200.from_dict(response.json())

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


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | UpdateIRPConfigResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: IRPConfig,
    entity_id: UUID | Unset = UNSET,
) -> Response[Error | UpdateIRPConfigResponse200]:
    """Create or update IRP credentials

     Upserts IRP credentials for the tenant. `environment` defaults to `sandbox`.

    Args:
        entity_id (UUID | Unset):
        body (IRPConfig):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | UpdateIRPConfigResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
        entity_id=entity_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: IRPConfig,
    entity_id: UUID | Unset = UNSET,
) -> Error | UpdateIRPConfigResponse200 | None:
    """Create or update IRP credentials

     Upserts IRP credentials for the tenant. `environment` defaults to `sandbox`.

    Args:
        entity_id (UUID | Unset):
        body (IRPConfig):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | UpdateIRPConfigResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
        entity_id=entity_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: IRPConfig,
    entity_id: UUID | Unset = UNSET,
) -> Response[Error | UpdateIRPConfigResponse200]:
    """Create or update IRP credentials

     Upserts IRP credentials for the tenant. `environment` defaults to `sandbox`.

    Args:
        entity_id (UUID | Unset):
        body (IRPConfig):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | UpdateIRPConfigResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
        entity_id=entity_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: IRPConfig,
    entity_id: UUID | Unset = UNSET,
) -> Error | UpdateIRPConfigResponse200 | None:
    """Create or update IRP credentials

     Upserts IRP credentials for the tenant. `environment` defaults to `sandbox`.

    Args:
        entity_id (UUID | Unset):
        body (IRPConfig):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | UpdateIRPConfigResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            entity_id=entity_id,
        )
    ).parsed
