from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Wallet")


@_attrs_define
class Wallet:
    """Prepaid balance per customer+currency, drained before credit notes and the gateway at invoice time. Amounts are
    minor units.

        Attributes:
            id (UUID | Unset):
            customer_id (UUID | Unset):
            currency (str | Unset):
            balance (int | Unset):
            auto_recharge_threshold (int | None | Unset):
            auto_recharge_amount (int | None | Unset):
            created_at (datetime.datetime | Unset):
            updated_at (datetime.datetime | Unset):
    """

    id: UUID | Unset = UNSET
    customer_id: UUID | Unset = UNSET
    currency: str | Unset = UNSET
    balance: int | Unset = UNSET
    auto_recharge_threshold: int | None | Unset = UNSET
    auto_recharge_amount: int | None | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        customer_id: str | Unset = UNSET
        if not isinstance(self.customer_id, Unset):
            customer_id = str(self.customer_id)

        currency = self.currency

        balance = self.balance

        auto_recharge_threshold: int | None | Unset
        if isinstance(self.auto_recharge_threshold, Unset):
            auto_recharge_threshold = UNSET
        else:
            auto_recharge_threshold = self.auto_recharge_threshold

        auto_recharge_amount: int | None | Unset
        if isinstance(self.auto_recharge_amount, Unset):
            auto_recharge_amount = UNSET
        else:
            auto_recharge_amount = self.auto_recharge_amount

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if customer_id is not UNSET:
            field_dict["customer_id"] = customer_id
        if currency is not UNSET:
            field_dict["currency"] = currency
        if balance is not UNSET:
            field_dict["balance"] = balance
        if auto_recharge_threshold is not UNSET:
            field_dict["auto_recharge_threshold"] = auto_recharge_threshold
        if auto_recharge_amount is not UNSET:
            field_dict["auto_recharge_amount"] = auto_recharge_amount
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

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

        _customer_id = d.pop("customer_id", UNSET)
        customer_id: UUID | Unset
        if isinstance(_customer_id, Unset):
            customer_id = UNSET
        else:
            customer_id = UUID(_customer_id)

        currency = d.pop("currency", UNSET)

        balance = d.pop("balance", UNSET)

        def _parse_auto_recharge_threshold(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        auto_recharge_threshold = _parse_auto_recharge_threshold(d.pop("auto_recharge_threshold", UNSET))

        def _parse_auto_recharge_amount(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        auto_recharge_amount = _parse_auto_recharge_amount(d.pop("auto_recharge_amount", UNSET))

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = datetime.datetime.fromisoformat(_updated_at)

        wallet = cls(
            id=id,
            customer_id=customer_id,
            currency=currency,
            balance=balance,
            auto_recharge_threshold=auto_recharge_threshold,
            auto_recharge_amount=auto_recharge_amount,
            created_at=created_at,
            updated_at=updated_at,
        )

        wallet.additional_properties = d
        return wallet

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
