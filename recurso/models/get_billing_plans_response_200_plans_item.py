from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetBillingPlansResponse200PlansItem")


@_attrs_define
class GetBillingPlansResponse200PlansItem:
    """
    Attributes:
        tier (str | Unset):
        name (str | Unset):
        price (str | Unset):
        period (str | Unset):
        free_note (str | Unset):
        features (list[str] | Unset):
        cta (str | Unset):
        recommended (bool | Unset):
    """

    tier: str | Unset = UNSET
    name: str | Unset = UNSET
    price: str | Unset = UNSET
    period: str | Unset = UNSET
    free_note: str | Unset = UNSET
    features: list[str] | Unset = UNSET
    cta: str | Unset = UNSET
    recommended: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tier = self.tier

        name = self.name

        price = self.price

        period = self.period

        free_note = self.free_note

        features: list[str] | Unset = UNSET
        if not isinstance(self.features, Unset):
            features = self.features

        cta = self.cta

        recommended = self.recommended

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tier is not UNSET:
            field_dict["tier"] = tier
        if name is not UNSET:
            field_dict["name"] = name
        if price is not UNSET:
            field_dict["price"] = price
        if period is not UNSET:
            field_dict["period"] = period
        if free_note is not UNSET:
            field_dict["free_note"] = free_note
        if features is not UNSET:
            field_dict["features"] = features
        if cta is not UNSET:
            field_dict["cta"] = cta
        if recommended is not UNSET:
            field_dict["recommended"] = recommended

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tier = d.pop("tier", UNSET)

        name = d.pop("name", UNSET)

        price = d.pop("price", UNSET)

        period = d.pop("period", UNSET)

        free_note = d.pop("free_note", UNSET)

        features = cast(list[str], d.pop("features", UNSET))

        cta = d.pop("cta", UNSET)

        recommended = d.pop("recommended", UNSET)

        get_billing_plans_response_200_plans_item = cls(
            tier=tier,
            name=name,
            price=price,
            period=period,
            free_note=free_note,
            features=features,
            cta=cta,
            recommended=recommended,
        )

        get_billing_plans_response_200_plans_item.additional_properties = d
        return get_billing_plans_response_200_plans_item

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
