from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.charge_input import ChargeInput
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    id: UUID,
    *,
    body: list[ChargeInput],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/plans/{id}/charges".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = []
    for body_item_data in body:
        body_item = body_item_data.to_dict()
        _kwargs["json"].append(body_item)

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | None:
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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error]:
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
    body: list[ChargeInput],
) -> Response[Error]:
    """Replace a plan's usage charge set

     Full replacement (like entitlements) — charges absent from the request are removed. Flat
    subscription fees stay on the plan's prices; a plan holding both is hybrid: flat fee billed in
    advance, usage billed in arrears at period close.

    Args:
        id (UUID):
        body (list[ChargeInput]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error]
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
    body: list[ChargeInput],
) -> Error | None:
    """Replace a plan's usage charge set

     Full replacement (like entitlements) — charges absent from the request are removed. Flat
    subscription fees stay on the plan's prices; a plan holding both is hybrid: flat fee billed in
    advance, usage billed in arrears at period close.

    Args:
        id (UUID):
        body (list[ChargeInput]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error
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
    body: list[ChargeInput],
) -> Response[Error]:
    """Replace a plan's usage charge set

     Full replacement (like entitlements) — charges absent from the request are removed. Flat
    subscription fees stay on the plan's prices; a plan holding both is hybrid: flat fee billed in
    advance, usage billed in arrears at period close.

    Args:
        id (UUID):
        body (list[ChargeInput]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: list[ChargeInput],
) -> Error | None:
    """Replace a plan's usage charge set

     Full replacement (like entitlements) — charges absent from the request are removed. Flat
    subscription fees stay on the plan's prices; a plan holding both is hybrid: flat fee billed in
    advance, usage billed in arrears at period close.

    Args:
        id (UUID):
        body (list[ChargeInput]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
