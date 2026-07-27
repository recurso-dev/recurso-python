from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.accounting_o_auth_callback_provider import AccountingOAuthCallbackProvider
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    provider: AccountingOAuthCallbackProvider,
    *,
    code: str,
    state: str,
    realm_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["code"] = code

    params["state"] = state

    params["realmId"] = realm_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/accounting/callback/{provider}".format(
            provider=quote(str(provider), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Error | None:
    if response.status_code == 302:
        response_302 = cast(Any, None)
        return response_302

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    provider: AccountingOAuthCallbackProvider,
    *,
    client: AuthenticatedClient | Client,
    code: str,
    state: str,
    realm_id: str | Unset = UNSET,
) -> Response[Any | Error]:
    """OAuth callback for accounting providers

     Redirect target for QuickBooks/Xero. Exchanges the authorization code for tokens, stores (or
    refreshes) the connection, and 302-redirects the browser back to the dashboard's Integrations page —
    `{DASHBOARD_URL}/integrations?connected={provider}` on success, or `?error={code}` (missing_code,
    invalid_state, unsupported_provider, exchange_failed, org_lookup_failed, save_failed) on failure.

    Args:
        provider (AccountingOAuthCallbackProvider):
        code (str):
        state (str):
        realm_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
    """

    kwargs = _get_kwargs(
        provider=provider,
        code=code,
        state=state,
        realm_id=realm_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    provider: AccountingOAuthCallbackProvider,
    *,
    client: AuthenticatedClient | Client,
    code: str,
    state: str,
    realm_id: str | Unset = UNSET,
) -> Any | Error | None:
    """OAuth callback for accounting providers

     Redirect target for QuickBooks/Xero. Exchanges the authorization code for tokens, stores (or
    refreshes) the connection, and 302-redirects the browser back to the dashboard's Integrations page —
    `{DASHBOARD_URL}/integrations?connected={provider}` on success, or `?error={code}` (missing_code,
    invalid_state, unsupported_provider, exchange_failed, org_lookup_failed, save_failed) on failure.

    Args:
        provider (AccountingOAuthCallbackProvider):
        code (str):
        state (str):
        realm_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
    """

    return sync_detailed(
        provider=provider,
        client=client,
        code=code,
        state=state,
        realm_id=realm_id,
    ).parsed


async def asyncio_detailed(
    provider: AccountingOAuthCallbackProvider,
    *,
    client: AuthenticatedClient | Client,
    code: str,
    state: str,
    realm_id: str | Unset = UNSET,
) -> Response[Any | Error]:
    """OAuth callback for accounting providers

     Redirect target for QuickBooks/Xero. Exchanges the authorization code for tokens, stores (or
    refreshes) the connection, and 302-redirects the browser back to the dashboard's Integrations page —
    `{DASHBOARD_URL}/integrations?connected={provider}` on success, or `?error={code}` (missing_code,
    invalid_state, unsupported_provider, exchange_failed, org_lookup_failed, save_failed) on failure.

    Args:
        provider (AccountingOAuthCallbackProvider):
        code (str):
        state (str):
        realm_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
    """

    kwargs = _get_kwargs(
        provider=provider,
        code=code,
        state=state,
        realm_id=realm_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    provider: AccountingOAuthCallbackProvider,
    *,
    client: AuthenticatedClient | Client,
    code: str,
    state: str,
    realm_id: str | Unset = UNSET,
) -> Any | Error | None:
    """OAuth callback for accounting providers

     Redirect target for QuickBooks/Xero. Exchanges the authorization code for tokens, stores (or
    refreshes) the connection, and 302-redirects the browser back to the dashboard's Integrations page —
    `{DASHBOARD_URL}/integrations?connected={provider}` on success, or `?error={code}` (missing_code,
    invalid_state, unsupported_provider, exchange_failed, org_lookup_failed, save_failed) on failure.

    Args:
        provider (AccountingOAuthCallbackProvider):
        code (str):
        state (str):
        realm_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
    """

    return (
        await asyncio_detailed(
            provider=provider,
            client=client,
            code=code,
            state=state,
            realm_id=realm_id,
        )
    ).parsed
