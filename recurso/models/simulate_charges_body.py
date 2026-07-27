from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.charge_input import ChargeInput
    from ..models.simulate_charges_body_usage_item import SimulateChargesBodyUsageItem


T = TypeVar("T", bound="SimulateChargesBody")


@_attrs_define
class SimulateChargesBody:
    """
    Attributes:
        currency (str | Unset): ISO code; defaults to the plan's first price currency.
        subscription_id (UUID | Unset): Optional: fills usage for metrics without an explicit entry.
        charges (list[ChargeInput] | Unset):
        usage (list[SimulateChargesBodyUsageItem] | Unset):
    """

    currency: str | Unset = UNSET
    subscription_id: UUID | Unset = UNSET
    charges: list[ChargeInput] | Unset = UNSET
    usage: list[SimulateChargesBodyUsageItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        currency = self.currency

        subscription_id: str | Unset = UNSET
        if not isinstance(self.subscription_id, Unset):
            subscription_id = str(self.subscription_id)

        charges: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.charges, Unset):
            charges = []
            for charges_item_data in self.charges:
                charges_item = charges_item_data.to_dict()
                charges.append(charges_item)

        usage: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.usage, Unset):
            usage = []
            for usage_item_data in self.usage:
                usage_item = usage_item_data.to_dict()
                usage.append(usage_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if currency is not UNSET:
            field_dict["currency"] = currency
        if subscription_id is not UNSET:
            field_dict["subscription_id"] = subscription_id
        if charges is not UNSET:
            field_dict["charges"] = charges
        if usage is not UNSET:
            field_dict["usage"] = usage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.charge_input import ChargeInput
        from ..models.simulate_charges_body_usage_item import SimulateChargesBodyUsageItem

        d = dict(src_dict)
        currency = d.pop("currency", UNSET)

        _subscription_id = d.pop("subscription_id", UNSET)
        subscription_id: UUID | Unset
        if isinstance(_subscription_id, Unset):
            subscription_id = UNSET
        else:
            subscription_id = UUID(_subscription_id)

        _charges = d.pop("charges", UNSET)
        charges: list[ChargeInput] | Unset = UNSET
        if _charges is not UNSET:
            charges = []
            for charges_item_data in _charges:
                charges_item = ChargeInput.from_dict(charges_item_data)

                charges.append(charges_item)

        _usage = d.pop("usage", UNSET)
        usage: list[SimulateChargesBodyUsageItem] | Unset = UNSET
        if _usage is not UNSET:
            usage = []
            for usage_item_data in _usage:
                usage_item = SimulateChargesBodyUsageItem.from_dict(usage_item_data)

                usage.append(usage_item)

        simulate_charges_body = cls(
            currency=currency,
            subscription_id=subscription_id,
            charges=charges,
            usage=usage,
        )

        simulate_charges_body.additional_properties = d
        return simulate_charges_body

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
