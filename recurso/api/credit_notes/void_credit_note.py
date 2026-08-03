from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.void_credit_note_response_200 import VoidCreditNoteResponse200
from ...types import Response


def _get_kwargs(
    id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/credit-notes/{id}/void".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | VoidCreditNoteResponse200 | None:
    if response.status_code == 200:
        response_200 = VoidCreditNoteResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | VoidCreditNoteResponse200]:
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
) -> Response[Error | VoidCreditNoteResponse200]:
    """Void an issued account-credit note

     Cancels an issued adjustment (account-credit) note and writes off its unspent balance, posting the
    GL reversal. Only the unspent portion is reversed; any already-applied credit stays real. Refund
    notes cannot be voided (the money left through the payment gateway). Admins/owners only.

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | VoidCreditNoteResponse200]
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
) -> Error | VoidCreditNoteResponse200 | None:
    """Void an issued account-credit note

     Cancels an issued adjustment (account-credit) note and writes off its unspent balance, posting the
    GL reversal. Only the unspent portion is reversed; any already-applied credit stays real. Refund
    notes cannot be voided (the money left through the payment gateway). Admins/owners only.

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | VoidCreditNoteResponse200
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Error | VoidCreditNoteResponse200]:
    """Void an issued account-credit note

     Cancels an issued adjustment (account-credit) note and writes off its unspent balance, posting the
    GL reversal. Only the unspent portion is reversed; any already-applied credit stays real. Refund
    notes cannot be voided (the money left through the payment gateway). Admins/owners only.

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | VoidCreditNoteResponse200]
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
) -> Error | VoidCreditNoteResponse200 | None:
    """Void an issued account-credit note

     Cancels an issued adjustment (account-credit) note and writes off its unspent balance, posting the
    GL reversal. Only the unspent portion is reversed; any already-applied credit stays real. Refund
    notes cannot be voided (the money left through the payment gateway). Admins/owners only.

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | VoidCreditNoteResponse200
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
