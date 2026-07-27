import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.get_tax_liability_report_response_200 import GetTaxLiabilityReportResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    year: int | Unset = UNSET,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["year"] = year

    json_from_: str | Unset = UNSET
    if not isinstance(from_, Unset):
        json_from_ = from_.isoformat()
    params["from"] = json_from_

    json_to: str | Unset = UNSET
    if not isinstance(to, Unset):
        json_to = to.isoformat()
    params["to"] = json_to

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/settings/tax/liability",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | GetTaxLiabilityReportResponse200 | None:
    if response.status_code == 200:
        response_200 = GetTaxLiabilityReportResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | GetTaxLiabilityReportResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    year: int | Unset = UNSET,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
) -> Response[Error | GetTaxLiabilityReportResponse200]:
    """Per-state US sales-tax liability report

     Per-state US sales-tax liability for a filing period: gross sales, the taxable/non-taxable split (by
    whether tax was collected), tax collected, invoice count, and whether the tenant has nexus in each
    state. Period is from+to (to exclusive) or year (defaults to the current calendar year). Scoped to
    US buyers, USD, non-void/draft invoices — ties to the nexus figures. Sales split into taxable (tax
    collected), exempt (a customer exemption applied), and non-taxable (no-nexus / below-threshold).

    Args:
        year (int | Unset):
        from_ (datetime.date | Unset):
        to (datetime.date | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetTaxLiabilityReportResponse200]
    """

    kwargs = _get_kwargs(
        year=year,
        from_=from_,
        to=to,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    year: int | Unset = UNSET,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
) -> Error | GetTaxLiabilityReportResponse200 | None:
    """Per-state US sales-tax liability report

     Per-state US sales-tax liability for a filing period: gross sales, the taxable/non-taxable split (by
    whether tax was collected), tax collected, invoice count, and whether the tenant has nexus in each
    state. Period is from+to (to exclusive) or year (defaults to the current calendar year). Scoped to
    US buyers, USD, non-void/draft invoices — ties to the nexus figures. Sales split into taxable (tax
    collected), exempt (a customer exemption applied), and non-taxable (no-nexus / below-threshold).

    Args:
        year (int | Unset):
        from_ (datetime.date | Unset):
        to (datetime.date | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetTaxLiabilityReportResponse200
    """

    return sync_detailed(
        client=client,
        year=year,
        from_=from_,
        to=to,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    year: int | Unset = UNSET,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
) -> Response[Error | GetTaxLiabilityReportResponse200]:
    """Per-state US sales-tax liability report

     Per-state US sales-tax liability for a filing period: gross sales, the taxable/non-taxable split (by
    whether tax was collected), tax collected, invoice count, and whether the tenant has nexus in each
    state. Period is from+to (to exclusive) or year (defaults to the current calendar year). Scoped to
    US buyers, USD, non-void/draft invoices — ties to the nexus figures. Sales split into taxable (tax
    collected), exempt (a customer exemption applied), and non-taxable (no-nexus / below-threshold).

    Args:
        year (int | Unset):
        from_ (datetime.date | Unset):
        to (datetime.date | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetTaxLiabilityReportResponse200]
    """

    kwargs = _get_kwargs(
        year=year,
        from_=from_,
        to=to,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    year: int | Unset = UNSET,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
) -> Error | GetTaxLiabilityReportResponse200 | None:
    """Per-state US sales-tax liability report

     Per-state US sales-tax liability for a filing period: gross sales, the taxable/non-taxable split (by
    whether tax was collected), tax collected, invoice count, and whether the tenant has nexus in each
    state. Period is from+to (to exclusive) or year (defaults to the current calendar year). Scoped to
    US buyers, USD, non-void/draft invoices — ties to the nexus figures. Sales split into taxable (tax
    collected), exempt (a customer exemption applied), and non-taxable (no-nexus / below-threshold).

    Args:
        year (int | Unset):
        from_ (datetime.date | Unset):
        to (datetime.date | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetTaxLiabilityReportResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            year=year,
            from_=from_,
            to=to,
        )
    ).parsed
