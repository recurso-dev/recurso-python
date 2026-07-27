from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.plan import Plan
from ...models.update_plan_body import UpdatePlanBody
from ...types import Response


def _get_kwargs(
    id: UUID,
    *,
    body: UpdatePlanBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/plans/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | Plan | None:
    if response.status_code == 200:
        response_200 = Plan.from_dict(response.json())

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | Plan]:
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
    body: UpdatePlanBody,
) -> Response[Error | Plan]:
    """Update or archive a plan

     Partial update of mutable plan fields — omitted fields are left unchanged. Set `active: false` to
    archive the plan (hides it from new subscriptions without affecting existing ones) and `true` to
    restore it. The plan's price/amount is a separate versioned entity and is not editable here.

    Args:
        id (UUID):
        body (UpdatePlanBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Plan]
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
    body: UpdatePlanBody,
) -> Error | Plan | None:
    """Update or archive a plan

     Partial update of mutable plan fields — omitted fields are left unchanged. Set `active: false` to
    archive the plan (hides it from new subscriptions without affecting existing ones) and `true` to
    restore it. The plan's price/amount is a separate versioned entity and is not editable here.

    Args:
        id (UUID):
        body (UpdatePlanBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Plan
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
    body: UpdatePlanBody,
) -> Response[Error | Plan]:
    """Update or archive a plan

     Partial update of mutable plan fields — omitted fields are left unchanged. Set `active: false` to
    archive the plan (hides it from new subscriptions without affecting existing ones) and `true` to
    restore it. The plan's price/amount is a separate versioned entity and is not editable here.

    Args:
        id (UUID):
        body (UpdatePlanBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Plan]
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
    body: UpdatePlanBody,
) -> Error | Plan | None:
    """Update or archive a plan

     Partial update of mutable plan fields — omitted fields are left unchanged. Set `active: false` to
    archive the plan (hides it from new subscriptions without affecting existing ones) and `true` to
    restore it. The plan's price/amount is a separate versioned entity and is not editable here.

    Args:
        id (UUID):
        body (UpdatePlanBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Plan
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
