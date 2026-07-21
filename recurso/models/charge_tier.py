from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChargeTier")


@_attrs_define
class ChargeTier:
    """
    Attributes:
        up_to (int | None): Inclusive upper unit bound; null = unbounded (last tier only).
        unit_amount (str | Unset): (graduated/volume) per-unit rate as a decimal string in MAJOR currency units
            (e.g. "0.0035").
        rate (str | Unset): (graduated_percentage) percent applied to this band of the base, decimal string e.g. "2.5".
        flat_amount (int | Unset): Minor units, added once when any unit lands in the tier.
    """

    up_to: int | None
    unit_amount: str | Unset = UNSET
    rate: str | Unset = UNSET
    flat_amount: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        up_to: int | None
        up_to = self.up_to

        unit_amount = self.unit_amount

        rate = self.rate

        flat_amount = self.flat_amount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "up_to": up_to,
            }
        )
        if unit_amount is not UNSET:
            field_dict["unit_amount"] = unit_amount
        if rate is not UNSET:
            field_dict["rate"] = rate
        if flat_amount is not UNSET:
            field_dict["flat_amount"] = flat_amount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_up_to(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        up_to = _parse_up_to(d.pop("up_to"))

        unit_amount = d.pop("unit_amount", UNSET)

        rate = d.pop("rate", UNSET)

        flat_amount = d.pop("flat_amount", UNSET)

        charge_tier = cls(
            up_to=up_to,
            unit_amount=unit_amount,
            rate=rate,
            flat_amount=flat_amount,
        )

        charge_tier.additional_properties = d
        return charge_tier

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
