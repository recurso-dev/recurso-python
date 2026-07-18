from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_usage_alert_body import CreateUsageAlertBody
from ...models.create_usage_alert_response_201 import CreateUsageAlertResponse201
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    *,
    body: CreateUsageAlertBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/usage-alerts",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | CreateUsageAlertResponse201 | Error | None:
    if response.status_code == 201:
        response_201 = CreateUsageAlertResponse201.from_dict(response.json())

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
) -> Response[Any | CreateUsageAlertResponse201 | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateUsageAlertBody,
) -> Response[Any | CreateUsageAlertResponse201 | Error]:
    """Create a usage threshold alert

     Fires at most once per billing period per threshold when the subscription's aggregated usage for the
    metric crosses it — via the `usage.alert.triggered` webhook event plus an email. `threshold_type` is
    `quantity` (absolute) or `percent_of_limit` (percentage of the entitlement limit whose feature_key
    equals the metric code; values above 100 alert on overage).

    Args:
        body (CreateUsageAlertBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateUsageAlertResponse201 | Error]
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
    body: CreateUsageAlertBody,
) -> Any | CreateUsageAlertResponse201 | Error | None:
    """Create a usage threshold alert

     Fires at most once per billing period per threshold when the subscription's aggregated usage for the
    metric crosses it — via the `usage.alert.triggered` webhook event plus an email. `threshold_type` is
    `quantity` (absolute) or `percent_of_limit` (percentage of the entitlement limit whose feature_key
    equals the metric code; values above 100 alert on overage).

    Args:
        body (CreateUsageAlertBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateUsageAlertResponse201 | Error
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateUsageAlertBody,
) -> Response[Any | CreateUsageAlertResponse201 | Error]:
    """Create a usage threshold alert

     Fires at most once per billing period per threshold when the subscription's aggregated usage for the
    metric crosses it — via the `usage.alert.triggered` webhook event plus an email. `threshold_type` is
    `quantity` (absolute) or `percent_of_limit` (percentage of the entitlement limit whose feature_key
    equals the metric code; values above 100 alert on overage).

    Args:
        body (CreateUsageAlertBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateUsageAlertResponse201 | Error]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateUsageAlertBody,
) -> Any | CreateUsageAlertResponse201 | Error | None:
    """Create a usage threshold alert

     Fires at most once per billing period per threshold when the subscription's aggregated usage for the
    metric crosses it — via the `usage.alert.triggered` webhook event plus an email. `threshold_type` is
    `quantity` (absolute) or `percent_of_limit` (percentage of the entitlement limit whose feature_key
    equals the metric code; values above 100 alert on overage).

    Args:
        body (CreateUsageAlertBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateUsageAlertResponse201 | Error
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
