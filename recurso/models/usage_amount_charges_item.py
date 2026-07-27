from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UsageAmountChargesItem")


@_attrs_define
class UsageAmountChargesItem:
    """
    Attributes:
        metric_code (str | Unset):
        metric_name (str | Unset):
        aggregation_type (str | Unset):
        charge_model (str | Unset):
        quantity (int | Unset):
        amount (int | Unset): Minor currency units.
    """

    metric_code: str | Unset = UNSET
    metric_name: str | Unset = UNSET
    aggregation_type: str | Unset = UNSET
    charge_model: str | Unset = UNSET
    quantity: int | Unset = UNSET
    amount: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        metric_code = self.metric_code

        metric_name = self.metric_name

        aggregation_type = self.aggregation_type

        charge_model = self.charge_model

        quantity = self.quantity

        amount = self.amount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if metric_code is not UNSET:
            field_dict["metric_code"] = metric_code
        if metric_name is not UNSET:
            field_dict["metric_name"] = metric_name
        if aggregation_type is not UNSET:
            field_dict["aggregation_type"] = aggregation_type
        if charge_model is not UNSET:
            field_dict["charge_model"] = charge_model
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if amount is not UNSET:
            field_dict["amount"] = amount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        metric_code = d.pop("metric_code", UNSET)

        metric_name = d.pop("metric_name", UNSET)

        aggregation_type = d.pop("aggregation_type", UNSET)

        charge_model = d.pop("charge_model", UNSET)

        quantity = d.pop("quantity", UNSET)

        amount = d.pop("amount", UNSET)

        usage_amount_charges_item = cls(
            metric_code=metric_code,
            metric_name=metric_name,
            aggregation_type=aggregation_type,
            charge_model=charge_model,
            quantity=quantity,
            amount=amount,
        )

        usage_amount_charges_item.additional_properties = d
        return usage_amount_charges_item

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
