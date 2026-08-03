from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.preview_chargebee_import_body import PreviewChargebeeImportBody
from ...models.preview_chargebee_import_response_200 import PreviewChargebeeImportResponse200
from ...types import Response


def _get_kwargs(
    *,
    body: PreviewChargebeeImportBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/import/chargebee/preview",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | PreviewChargebeeImportResponse200 | None:
    if response.status_code == 200:
        response_200 = PreviewChargebeeImportResponse200.from_dict(response.json())

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
) -> Response[Error | PreviewChargebeeImportResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PreviewChargebeeImportBody,
) -> Response[Error | PreviewChargebeeImportResponse200]:
    """Dry-run preview of a Chargebee export

     Parses an uploaded Chargebee export (customers, plans, subscriptions) and returns a plan of what a
    commit would create, link, skip, or refuse — with NO side effects. Existing customers are matched by
    email.

    Args:
        body (PreviewChargebeeImportBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PreviewChargebeeImportResponse200]
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
    body: PreviewChargebeeImportBody,
) -> Error | PreviewChargebeeImportResponse200 | None:
    """Dry-run preview of a Chargebee export

     Parses an uploaded Chargebee export (customers, plans, subscriptions) and returns a plan of what a
    commit would create, link, skip, or refuse — with NO side effects. Existing customers are matched by
    email.

    Args:
        body (PreviewChargebeeImportBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PreviewChargebeeImportResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PreviewChargebeeImportBody,
) -> Response[Error | PreviewChargebeeImportResponse200]:
    """Dry-run preview of a Chargebee export

     Parses an uploaded Chargebee export (customers, plans, subscriptions) and returns a plan of what a
    commit would create, link, skip, or refuse — with NO side effects. Existing customers are matched by
    email.

    Args:
        body (PreviewChargebeeImportBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PreviewChargebeeImportResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PreviewChargebeeImportBody,
) -> Error | PreviewChargebeeImportResponse200 | None:
    """Dry-run preview of a Chargebee export

     Parses an uploaded Chargebee export (customers, plans, subscriptions) and returns a plan of what a
    commit would create, link, skip, or refuse — with NO side effects. Existing customers are matched by
    email.

    Args:
        body (PreviewChargebeeImportBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PreviewChargebeeImportResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
