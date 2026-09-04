from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_payment_attempts_response_200 import ListPaymentAttemptsResponse200
from ...models.list_payment_attempts_status import ListPaymentAttemptsStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    status: ListPaymentAttemptsStatus | Unset = UNSET,
    q: str | Unset = UNSET,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params["q"] = q

    params["page"] = page

    params["per_page"] = per_page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/payment-attempts",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ListPaymentAttemptsResponse200 | None:
    if response.status_code == 200:
        response_200 = ListPaymentAttemptsResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ListPaymentAttemptsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    status: ListPaymentAttemptsStatus | Unset = UNSET,
    q: str | Unset = UNSET,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
) -> Response[ListPaymentAttemptsResponse200]:
    """Payments log (tenant-wide payment attempts)

     Every gateway payment attempt for the tenant, newest first, paginated, with an optional status
    filter (initiated/processing/succeeded/failed/ returned). Each row carries its invoice number. The
    operator's failed- payments log. Read-only.

    Args:
        status (ListPaymentAttemptsStatus | Unset):
        q (str | Unset):
        page (int | Unset):
        per_page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListPaymentAttemptsResponse200]
    """

    kwargs = _get_kwargs(
        status=status,
        q=q,
        page=page,
        per_page=per_page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    status: ListPaymentAttemptsStatus | Unset = UNSET,
    q: str | Unset = UNSET,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
) -> ListPaymentAttemptsResponse200 | None:
    """Payments log (tenant-wide payment attempts)

     Every gateway payment attempt for the tenant, newest first, paginated, with an optional status
    filter (initiated/processing/succeeded/failed/ returned). Each row carries its invoice number. The
    operator's failed- payments log. Read-only.

    Args:
        status (ListPaymentAttemptsStatus | Unset):
        q (str | Unset):
        page (int | Unset):
        per_page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListPaymentAttemptsResponse200
    """

    return sync_detailed(
        client=client,
        status=status,
        q=q,
        page=page,
        per_page=per_page,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    status: ListPaymentAttemptsStatus | Unset = UNSET,
    q: str | Unset = UNSET,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
) -> Response[ListPaymentAttemptsResponse200]:
    """Payments log (tenant-wide payment attempts)

     Every gateway payment attempt for the tenant, newest first, paginated, with an optional status
    filter (initiated/processing/succeeded/failed/ returned). Each row carries its invoice number. The
    operator's failed- payments log. Read-only.

    Args:
        status (ListPaymentAttemptsStatus | Unset):
        q (str | Unset):
        page (int | Unset):
        per_page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListPaymentAttemptsResponse200]
    """

    kwargs = _get_kwargs(
        status=status,
        q=q,
        page=page,
        per_page=per_page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    status: ListPaymentAttemptsStatus | Unset = UNSET,
    q: str | Unset = UNSET,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
) -> ListPaymentAttemptsResponse200 | None:
    """Payments log (tenant-wide payment attempts)

     Every gateway payment attempt for the tenant, newest first, paginated, with an optional status
    filter (initiated/processing/succeeded/failed/ returned). Each row carries its invoice number. The
    operator's failed- payments log. Read-only.

    Args:
        status (ListPaymentAttemptsStatus | Unset):
        q (str | Unset):
        page (int | Unset):
        per_page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListPaymentAttemptsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            status=status,
            q=q,
            page=page,
            per_page=per_page,
        )
    ).parsed
