from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.billable_metric_input import BillableMetricInput
from ...models.create_billable_metric_response_201 import CreateBillableMetricResponse201
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    *,
    body: BillableMetricInput,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/billable-metrics",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | CreateBillableMetricResponse201 | Error | None:
    if response.status_code == 201:
        response_201 = CreateBillableMetricResponse201.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 409:
        response_409 = cast(Any, None)
        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | CreateBillableMetricResponse201 | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BillableMetricInput,
) -> Response[Any | CreateBillableMetricResponse201 | Error]:
    """Create a billable metric

     A metric is a tenant-defined meter over usage events; its `code` doubles as the event `dimension` it
    aggregates. Aggregations: `count`, `sum`, `max`, `unique` (distinct values of the event property
    named by `field_name`).

    Args:
        body (BillableMetricInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateBillableMetricResponse201 | Error]
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
    body: BillableMetricInput,
) -> Any | CreateBillableMetricResponse201 | Error | None:
    """Create a billable metric

     A metric is a tenant-defined meter over usage events; its `code` doubles as the event `dimension` it
    aggregates. Aggregations: `count`, `sum`, `max`, `unique` (distinct values of the event property
    named by `field_name`).

    Args:
        body (BillableMetricInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateBillableMetricResponse201 | Error
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BillableMetricInput,
) -> Response[Any | CreateBillableMetricResponse201 | Error]:
    """Create a billable metric

     A metric is a tenant-defined meter over usage events; its `code` doubles as the event `dimension` it
    aggregates. Aggregations: `count`, `sum`, `max`, `unique` (distinct values of the event property
    named by `field_name`).

    Args:
        body (BillableMetricInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateBillableMetricResponse201 | Error]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: BillableMetricInput,
) -> Any | CreateBillableMetricResponse201 | Error | None:
    """Create a billable metric

     A metric is a tenant-defined meter over usage events; its `code` doubles as the event `dimension` it
    aggregates. Aggregations: `count`, `sum`, `max`, `unique` (distinct values of the event property
    named by `field_name`).

    Args:
        body (BillableMetricInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateBillableMetricResponse201 | Error
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
