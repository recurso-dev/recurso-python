from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cancel_gift_response_200 import CancelGiftResponse200
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/gifts/{id}/cancel".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CancelGiftResponse200 | Error | None:
    if response.status_code == 200:
        response_200 = CancelGiftResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = Error.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CancelGiftResponse200 | Error]:
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
) -> Response[CancelGiftResponse200 | Error]:
    """Cancel an unredeemed gift (buyer gets account credit)

     Cancels a purchased-but-unredeemed gift. If the buyer's purchase invoice was PAID, a spendable
    adjustment credit note for the amount is issued to the buyer (through the normal credit-note path,
    so approval governance and ledger postings apply). If the invoice is still open, it is voided
    instead — no money arrived, nothing is credited. A redeemed gift cannot be canceled (409); a second
    cancel is refused (409) so the credit can never issue twice.

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CancelGiftResponse200 | Error]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> CancelGiftResponse200 | Error | None:
    """Cancel an unredeemed gift (buyer gets account credit)

     Cancels a purchased-but-unredeemed gift. If the buyer's purchase invoice was PAID, a spendable
    adjustment credit note for the amount is issued to the buyer (through the normal credit-note path,
    so approval governance and ledger postings apply). If the invoice is still open, it is voided
    instead — no money arrived, nothing is credited. A redeemed gift cannot be canceled (409); a second
    cancel is refused (409) so the credit can never issue twice.

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CancelGiftResponse200 | Error
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[CancelGiftResponse200 | Error]:
    """Cancel an unredeemed gift (buyer gets account credit)

     Cancels a purchased-but-unredeemed gift. If the buyer's purchase invoice was PAID, a spendable
    adjustment credit note for the amount is issued to the buyer (through the normal credit-note path,
    so approval governance and ledger postings apply). If the invoice is still open, it is voided
    instead — no money arrived, nothing is credited. A redeemed gift cannot be canceled (409); a second
    cancel is refused (409) so the credit can never issue twice.

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CancelGiftResponse200 | Error]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> CancelGiftResponse200 | Error | None:
    """Cancel an unredeemed gift (buyer gets account credit)

     Cancels a purchased-but-unredeemed gift. If the buyer's purchase invoice was PAID, a spendable
    adjustment credit note for the amount is issued to the buyer (through the normal credit-note path,
    so approval governance and ledger postings apply). If the invoice is still open, it is voided
    instead — no money arrived, nothing is credited. A redeemed gift cannot be canceled (409); a second
    cancel is refused (409) so the credit can never issue twice.

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CancelGiftResponse200 | Error
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
