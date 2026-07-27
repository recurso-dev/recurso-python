from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.record_usage_events_batch_body import RecordUsageEventsBatchBody
from ...models.record_usage_events_batch_response_200 import RecordUsageEventsBatchResponse200
from ...types import Response


def _get_kwargs(
    *,
    body: RecordUsageEventsBatchBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/usage/events/batch",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | RecordUsageEventsBatchResponse200 | None:
    if response.status_code == 200:
        response_200 = RecordUsageEventsBatchResponse200.from_dict(response.json())

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
) -> Response[Error | RecordUsageEventsBatchResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RecordUsageEventsBatchBody,
) -> Response[Error | RecordUsageEventsBatchResponse200]:
    r"""Record up to 500 usage events

     Per-item results — one bad event never fails the batch. Items with a `transaction_id` are idempotent
    (duplicates collapse to the original event with status \"duplicate\").

    Args:
        body (RecordUsageEventsBatchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | RecordUsageEventsBatchResponse200]
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
    body: RecordUsageEventsBatchBody,
) -> Error | RecordUsageEventsBatchResponse200 | None:
    r"""Record up to 500 usage events

     Per-item results — one bad event never fails the batch. Items with a `transaction_id` are idempotent
    (duplicates collapse to the original event with status \"duplicate\").

    Args:
        body (RecordUsageEventsBatchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | RecordUsageEventsBatchResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RecordUsageEventsBatchBody,
) -> Response[Error | RecordUsageEventsBatchResponse200]:
    r"""Record up to 500 usage events

     Per-item results — one bad event never fails the batch. Items with a `transaction_id` are idempotent
    (duplicates collapse to the original event with status \"duplicate\").

    Args:
        body (RecordUsageEventsBatchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | RecordUsageEventsBatchResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: RecordUsageEventsBatchBody,
) -> Error | RecordUsageEventsBatchResponse200 | None:
    r"""Record up to 500 usage events

     Per-item results — one bad event never fails the batch. Items with a `transaction_id` are idempotent
    (duplicates collapse to the original event with status \"duplicate\").

    Args:
        body (RecordUsageEventsBatchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | RecordUsageEventsBatchResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
