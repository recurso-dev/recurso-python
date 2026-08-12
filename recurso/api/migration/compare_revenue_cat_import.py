from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.compare_revenue_cat_import_body import CompareRevenueCatImportBody
from ...models.compare_revenue_cat_import_response_200 import CompareRevenueCatImportResponse200
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    *,
    body: CompareRevenueCatImportBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/import/revenuecat/compare",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CompareRevenueCatImportResponse200 | Error | None:
    if response.status_code == 200:
        response_200 = CompareRevenueCatImportResponse200.from_dict(response.json())

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
) -> Response[CompareRevenueCatImportResponse200 | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CompareRevenueCatImportBody,
) -> Response[CompareRevenueCatImportResponse200 | Error]:
    """Compare gate — prove the RevenueCat migration before cut-over

     Diffs the uploaded RevenueCat export against the tenant's live Recurso data with zero writes —
    coverage (subscribers with an email, active entitlements), fidelity (product price/currency/period;
    identity), and billing continuity (an entitlement whose expires_at drifted >1h from the imported
    period end is flagged). ready=true means zero issues.

    Args:
        body (CompareRevenueCatImportBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CompareRevenueCatImportResponse200 | Error]
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
    body: CompareRevenueCatImportBody,
) -> CompareRevenueCatImportResponse200 | Error | None:
    """Compare gate — prove the RevenueCat migration before cut-over

     Diffs the uploaded RevenueCat export against the tenant's live Recurso data with zero writes —
    coverage (subscribers with an email, active entitlements), fidelity (product price/currency/period;
    identity), and billing continuity (an entitlement whose expires_at drifted >1h from the imported
    period end is flagged). ready=true means zero issues.

    Args:
        body (CompareRevenueCatImportBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CompareRevenueCatImportResponse200 | Error
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CompareRevenueCatImportBody,
) -> Response[CompareRevenueCatImportResponse200 | Error]:
    """Compare gate — prove the RevenueCat migration before cut-over

     Diffs the uploaded RevenueCat export against the tenant's live Recurso data with zero writes —
    coverage (subscribers with an email, active entitlements), fidelity (product price/currency/period;
    identity), and billing continuity (an entitlement whose expires_at drifted >1h from the imported
    period end is flagged). ready=true means zero issues.

    Args:
        body (CompareRevenueCatImportBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CompareRevenueCatImportResponse200 | Error]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CompareRevenueCatImportBody,
) -> CompareRevenueCatImportResponse200 | Error | None:
    """Compare gate — prove the RevenueCat migration before cut-over

     Diffs the uploaded RevenueCat export against the tenant's live Recurso data with zero writes —
    coverage (subscribers with an email, active entitlements), fidelity (product price/currency/period;
    identity), and billing continuity (an entitlement whose expires_at drifted >1h from the imported
    period end is flagged). ready=true means zero issues.

    Args:
        body (CompareRevenueCatImportBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CompareRevenueCatImportResponse200 | Error
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
