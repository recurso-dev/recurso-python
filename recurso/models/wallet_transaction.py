from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.wallet_transaction_source import WalletTransactionSource
from ..models.wallet_transaction_type import WalletTransactionType
from ..types import UNSET, Unset

T = TypeVar("T", bound="WalletTransaction")


@_attrs_define
class WalletTransaction:
    """One append-only wallet movement with the balance after it.

    Attributes:
        id (UUID | Unset):
        wallet_id (UUID | Unset):
        type_ (WalletTransactionType | Unset):
        source (WalletTransactionSource | Unset):
        amount (int | Unset):
        remaining (int | None | Unset): Undrained residue of a top_up row.
        balance_after (int | Unset):
        invoice_id (None | Unset | UUID):
        expires_at (datetime.datetime | None | Unset):
        created_at (datetime.datetime | Unset):
    """

    id: UUID | Unset = UNSET
    wallet_id: UUID | Unset = UNSET
    type_: WalletTransactionType | Unset = UNSET
    source: WalletTransactionSource | Unset = UNSET
    amount: int | Unset = UNSET
    remaining: int | None | Unset = UNSET
    balance_after: int | Unset = UNSET
    invoice_id: None | Unset | UUID = UNSET
    expires_at: datetime.datetime | None | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        wallet_id: str | Unset = UNSET
        if not isinstance(self.wallet_id, Unset):
            wallet_id = str(self.wallet_id)

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        source: str | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value

        amount = self.amount

        remaining: int | None | Unset
        if isinstance(self.remaining, Unset):
            remaining = UNSET
        else:
            remaining = self.remaining

        balance_after = self.balance_after

        invoice_id: None | str | Unset
        if isinstance(self.invoice_id, Unset):
            invoice_id = UNSET
        elif isinstance(self.invoice_id, UUID):
            invoice_id = str(self.invoice_id)
        else:
            invoice_id = self.invoice_id

        expires_at: None | str | Unset
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        elif isinstance(self.expires_at, datetime.datetime):
            expires_at = self.expires_at.isoformat()
        else:
            expires_at = self.expires_at

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if wallet_id is not UNSET:
            field_dict["wallet_id"] = wallet_id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if source is not UNSET:
            field_dict["source"] = source
        if amount is not UNSET:
            field_dict["amount"] = amount
        if remaining is not UNSET:
            field_dict["remaining"] = remaining
        if balance_after is not UNSET:
            field_dict["balance_after"] = balance_after
        if invoice_id is not UNSET:
            field_dict["invoice_id"] = invoice_id
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        _wallet_id = d.pop("wallet_id", UNSET)
        wallet_id: UUID | Unset
        if isinstance(_wallet_id, Unset):
            wallet_id = UNSET
        else:
            wallet_id = UUID(_wallet_id)

        _type_ = d.pop("type", UNSET)
        type_: WalletTransactionType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = WalletTransactionType(_type_)

        _source = d.pop("source", UNSET)
        source: WalletTransactionSource | Unset
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = WalletTransactionSource(_source)

        amount = d.pop("amount", UNSET)

        def _parse_remaining(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        remaining = _parse_remaining(d.pop("remaining", UNSET))

        balance_after = d.pop("balance_after", UNSET)

        def _parse_invoice_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                invoice_id_type_0 = UUID(data)

                return invoice_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        invoice_id = _parse_invoice_id(d.pop("invoice_id", UNSET))

        def _parse_expires_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_at_type_0 = datetime.datetime.fromisoformat(data)

                return expires_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        expires_at = _parse_expires_at(d.pop("expires_at", UNSET))

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        wallet_transaction = cls(
            id=id,
            wallet_id=wallet_id,
            type_=type_,
            source=source,
            amount=amount,
            remaining=remaining,
            balance_after=balance_after,
            invoice_id=invoice_id,
            expires_at=expires_at,
            created_at=created_at,
        )

        wallet_transaction.additional_properties = d
        return wallet_transaction

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
