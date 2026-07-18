from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.usage_amount_charges_item import UsageAmountChargesItem


T = TypeVar("T", bound="UsageAmount")


@_attrs_define
class UsageAmount:
    """Live preview of the current period's usage priced as of now.

    Attributes:
        subscription_id (UUID | Unset):
        currency (str | Unset):
        current_period_start (datetime.datetime | Unset):
        as_of (datetime.datetime | Unset):
        charges (list[UsageAmountChargesItem] | Unset):
        total_amount (int | Unset):
    """

    subscription_id: UUID | Unset = UNSET
    currency: str | Unset = UNSET
    current_period_start: datetime.datetime | Unset = UNSET
    as_of: datetime.datetime | Unset = UNSET
    charges: list[UsageAmountChargesItem] | Unset = UNSET
    total_amount: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        subscription_id: str | Unset = UNSET
        if not isinstance(self.subscription_id, Unset):
            subscription_id = str(self.subscription_id)

        currency = self.currency

        current_period_start: str | Unset = UNSET
        if not isinstance(self.current_period_start, Unset):
            current_period_start = self.current_period_start.isoformat()

        as_of: str | Unset = UNSET
        if not isinstance(self.as_of, Unset):
            as_of = self.as_of.isoformat()

        charges: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.charges, Unset):
            charges = []
            for charges_item_data in self.charges:
                charges_item = charges_item_data.to_dict()
                charges.append(charges_item)

        total_amount = self.total_amount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if subscription_id is not UNSET:
            field_dict["subscription_id"] = subscription_id
        if currency is not UNSET:
            field_dict["currency"] = currency
        if current_period_start is not UNSET:
            field_dict["current_period_start"] = current_period_start
        if as_of is not UNSET:
            field_dict["as_of"] = as_of
        if charges is not UNSET:
            field_dict["charges"] = charges
        if total_amount is not UNSET:
            field_dict["total_amount"] = total_amount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.usage_amount_charges_item import UsageAmountChargesItem

        d = dict(src_dict)
        _subscription_id = d.pop("subscription_id", UNSET)
        subscription_id: UUID | Unset
        if isinstance(_subscription_id, Unset):
            subscription_id = UNSET
        else:
            subscription_id = UUID(_subscription_id)

        currency = d.pop("currency", UNSET)

        _current_period_start = d.pop("current_period_start", UNSET)
        current_period_start: datetime.datetime | Unset
        if isinstance(_current_period_start, Unset):
            current_period_start = UNSET
        else:
            current_period_start = datetime.datetime.fromisoformat(_current_period_start)

        _as_of = d.pop("as_of", UNSET)
        as_of: datetime.datetime | Unset
        if isinstance(_as_of, Unset):
            as_of = UNSET
        else:
            as_of = datetime.datetime.fromisoformat(_as_of)

        _charges = d.pop("charges", UNSET)
        charges: list[UsageAmountChargesItem] | Unset = UNSET
        if _charges is not UNSET:
            charges = []
            for charges_item_data in _charges:
                charges_item = UsageAmountChargesItem.from_dict(charges_item_data)

                charges.append(charges_item)

        total_amount = d.pop("total_amount", UNSET)

        usage_amount = cls(
            subscription_id=subscription_id,
            currency=currency,
            current_period_start=current_period_start,
            as_of=as_of,
            charges=charges,
            total_amount=total_amount,
        )

        usage_amount.additional_properties = d
        return usage_amount

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
