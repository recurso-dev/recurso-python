from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_invoice_journal_entries_response_200 import GetInvoiceJournalEntriesResponse200
from ...types import Response


def _get_kwargs(
    id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/invoices/{id}/journal-entries".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetInvoiceJournalEntriesResponse200 | None:
    if response.status_code == 200:
        response_200 = GetInvoiceJournalEntriesResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GetInvoiceJournalEntriesResponse200]:
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
) -> Response[Any | GetInvoiceJournalEntriesResponse200]:
    """Invoice journal entries (ledger drill)

     Every ledger posting that references this invoice — its Code-1 issuance, Code-6 tax reclass, Code-3
    payment, and any credit/refund/write-off legs — each as a transfer with its debit and credit account
    (code + name), amount, posting code, and timestamp. The finance-accounting side of the invoice page.
    Read-only; an existing invoice with no postings yet returns an empty list.

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetInvoiceJournalEntriesResponse200]
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
) -> Any | GetInvoiceJournalEntriesResponse200 | None:
    """Invoice journal entries (ledger drill)

     Every ledger posting that references this invoice — its Code-1 issuance, Code-6 tax reclass, Code-3
    payment, and any credit/refund/write-off legs — each as a transfer with its debit and credit account
    (code + name), amount, posting code, and timestamp. The finance-accounting side of the invoice page.
    Read-only; an existing invoice with no postings yet returns an empty list.

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetInvoiceJournalEntriesResponse200
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GetInvoiceJournalEntriesResponse200]:
    """Invoice journal entries (ledger drill)

     Every ledger posting that references this invoice — its Code-1 issuance, Code-6 tax reclass, Code-3
    payment, and any credit/refund/write-off legs — each as a transfer with its debit and credit account
    (code + name), amount, posting code, and timestamp. The finance-accounting side of the invoice page.
    Read-only; an existing invoice with no postings yet returns an empty list.

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetInvoiceJournalEntriesResponse200]
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
) -> Any | GetInvoiceJournalEntriesResponse200 | None:
    """Invoice journal entries (ledger drill)

     Every ledger posting that references this invoice — its Code-1 issuance, Code-6 tax reclass, Code-3
    payment, and any credit/refund/write-off legs — each as a transfer with its debit and credit account
    (code + name), amount, posting code, and timestamp. The finance-accounting side of the invoice page.
    Read-only; an existing invoice with no postings yet returns an empty list.

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetInvoiceJournalEntriesResponse200
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
