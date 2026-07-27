from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.update_usage_alert_body import UpdateUsageAlertBody
from ...models.update_usage_alert_response_200 import UpdateUsageAlertResponse200
from ...types import Response


def _get_kwargs(
    id: UUID,
    *,
    body: UpdateUsageAlertBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/usage-alerts/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | Error | UpdateUsageAlertResponse200 | None:
    if response.status_code == 200:
        response_200 = UpdateUsageAlertResponse200.from_dict(response.json())

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

    if response.status_code == 409:
        response_409 = cast(Any, None)
        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | Error | UpdateUsageAlertResponse200]:
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
    body: UpdateUsageAlertBody,
) -> Response[Any | Error | UpdateUsageAlertResponse200]:
    """Edit a usage alert's threshold

     Re-aims an existing alert at a new threshold (type and value). Subscription and metric are the
    alert's identity — to change those, delete and re-create. Editing resets the per-period fired dedup
    so the new threshold can fire in the current billing period.

    Args:
        id (UUID):
        body (UpdateUsageAlertBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error | UpdateUsageAlertResponse200]
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
    body: UpdateUsageAlertBody,
) -> Any | Error | UpdateUsageAlertResponse200 | None:
    """Edit a usage alert's threshold

     Re-aims an existing alert at a new threshold (type and value). Subscription and metric are the
    alert's identity — to change those, delete and re-create. Editing resets the per-period fired dedup
    so the new threshold can fire in the current billing period.

    Args:
        id (UUID):
        body (UpdateUsageAlertBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error | UpdateUsageAlertResponse200
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
    body: UpdateUsageAlertBody,
) -> Response[Any | Error | UpdateUsageAlertResponse200]:
    """Edit a usage alert's threshold

     Re-aims an existing alert at a new threshold (type and value). Subscription and metric are the
    alert's identity — to change those, delete and re-create. Editing resets the per-period fired dedup
    so the new threshold can fire in the current billing period.

    Args:
        id (UUID):
        body (UpdateUsageAlertBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error | UpdateUsageAlertResponse200]
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
    body: UpdateUsageAlertBody,
) -> Any | Error | UpdateUsageAlertResponse200 | None:
    """Edit a usage alert's threshold

     Re-aims an existing alert at a new threshold (type and value). Subscription and metric are the
    alert's identity — to change those, delete and re-create. Editing resets the per-period fired dedup
    so the new threshold can fire in the current billing period.

    Args:
        id (UUID):
        body (UpdateUsageAlertBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error | UpdateUsageAlertResponse200
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
