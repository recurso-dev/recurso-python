from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_billing_plans_response_200_plans_item import GetBillingPlansResponse200PlansItem


T = TypeVar("T", bound="GetBillingPlansResponse200")


@_attrs_define
class GetBillingPlansResponse200:
    """
    Attributes:
        plans (list[GetBillingPlansResponse200PlansItem] | Unset):
    """

    plans: list[GetBillingPlansResponse200PlansItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        plans: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.plans, Unset):
            plans = []
            for plans_item_data in self.plans:
                plans_item = plans_item_data.to_dict()
                plans.append(plans_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if plans is not UNSET:
            field_dict["plans"] = plans

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_billing_plans_response_200_plans_item import GetBillingPlansResponse200PlansItem

        d = dict(src_dict)
        _plans = d.pop("plans", UNSET)
        plans: list[GetBillingPlansResponse200PlansItem] | Unset = UNSET
        if _plans is not UNSET:
            plans = []
            for plans_item_data in _plans:
                plans_item = GetBillingPlansResponse200PlansItem.from_dict(plans_item_data)

                plans.append(plans_item)

        get_billing_plans_response_200 = cls(
            plans=plans,
        )

        get_billing_plans_response_200.additional_properties = d
        return get_billing_plans_response_200

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
