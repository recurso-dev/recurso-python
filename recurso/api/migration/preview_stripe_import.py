from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.preview_stripe_import_body import PreviewStripeImportBody
from ...models.preview_stripe_import_response_200 import PreviewStripeImportResponse200
from ...types import Response


def _get_kwargs(
    *,
    body: PreviewStripeImportBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/import/stripe/preview",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | PreviewStripeImportResponse200 | None:
    if response.status_code == 200:
        response_200 = PreviewStripeImportResponse200.from_dict(response.json())

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
) -> Response[Error | PreviewStripeImportResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PreviewStripeImportBody,
) -> Response[Error | PreviewStripeImportResponse200]:
    """Dry-run preview of a Stripe export

     Parses an uploaded Stripe export (customers, products, prices, subscriptions, payment methods) and
    returns a plan describing exactly what a commit would create, link to an existing record, skip, or
    refuse — with NO side effects. Existing customers are matched by email and linked rather than
    duplicated.

    Args:
        body (PreviewStripeImportBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PreviewStripeImportResponse200]
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
    body: PreviewStripeImportBody,
) -> Error | PreviewStripeImportResponse200 | None:
    """Dry-run preview of a Stripe export

     Parses an uploaded Stripe export (customers, products, prices, subscriptions, payment methods) and
    returns a plan describing exactly what a commit would create, link to an existing record, skip, or
    refuse — with NO side effects. Existing customers are matched by email and linked rather than
    duplicated.

    Args:
        body (PreviewStripeImportBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PreviewStripeImportResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PreviewStripeImportBody,
) -> Response[Error | PreviewStripeImportResponse200]:
    """Dry-run preview of a Stripe export

     Parses an uploaded Stripe export (customers, products, prices, subscriptions, payment methods) and
    returns a plan describing exactly what a commit would create, link to an existing record, skip, or
    refuse — with NO side effects. Existing customers are matched by email and linked rather than
    duplicated.

    Args:
        body (PreviewStripeImportBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PreviewStripeImportResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PreviewStripeImportBody,
) -> Error | PreviewStripeImportResponse200 | None:
    """Dry-run preview of a Stripe export

     Parses an uploaded Stripe export (customers, products, prices, subscriptions, payment methods) and
    returns a plan describing exactly what a commit would create, link to an existing record, skip, or
    refuse — with NO side effects. Existing customers are matched by email and linked rather than
    duplicated.

    Args:
        body (PreviewStripeImportBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PreviewStripeImportResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
