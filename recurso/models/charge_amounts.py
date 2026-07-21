from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.charge_tier import ChargeTier


T = TypeVar("T", bound="ChargeAmounts")


@_attrs_define
class ChargeAmounts:
    """Pricing properties for one currency; fields depend on the charge model.

    Attributes:
        unit_amount (str | Unset): (per_unit) decimal-string rate in MAJOR currency units.
        package_amount (int | Unset): (package) price in minor units per bundle.
        package_size (int | Unset): (package) units per bundle; partial bundles round up.
        tiers (list[ChargeTier] | Unset): (graduated/volume/graduated_percentage) price bands.
        rate (str | Unset): (percentage) percent applied to the base, decimal string e.g. "2.5".
        fixed_amount (int | Unset): (percentage) flat fee in minor units added after the percentage.
        free_units (int | Unset): (percentage) base units exempt from the percentage, deducted first.
        min_amount (int | Unset): (percentage) floor on the line in minor units; 0 = no floor.
        max_amount (int | Unset): (percentage) cap on the line in minor units; 0 = no cap.
    """

    unit_amount: str | Unset = UNSET
    package_amount: int | Unset = UNSET
    package_size: int | Unset = UNSET
    tiers: list["ChargeTier"] | Unset = UNSET
    rate: str | Unset = UNSET
    fixed_amount: int | Unset = UNSET
    free_units: int | Unset = UNSET
    min_amount: int | Unset = UNSET
    max_amount: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unit_amount = self.unit_amount

        package_amount = self.package_amount

        package_size = self.package_size

        tiers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tiers, Unset):
            tiers = []
            for tiers_item_data in self.tiers:
                tiers_item = tiers_item_data.to_dict()
                tiers.append(tiers_item)

        rate = self.rate

        fixed_amount = self.fixed_amount

        free_units = self.free_units

        min_amount = self.min_amount

        max_amount = self.max_amount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if unit_amount is not UNSET:
            field_dict["unit_amount"] = unit_amount
        if package_amount is not UNSET:
            field_dict["package_amount"] = package_amount
        if package_size is not UNSET:
            field_dict["package_size"] = package_size
        if tiers is not UNSET:
            field_dict["tiers"] = tiers
        if rate is not UNSET:
            field_dict["rate"] = rate
        if fixed_amount is not UNSET:
            field_dict["fixed_amount"] = fixed_amount
        if free_units is not UNSET:
            field_dict["free_units"] = free_units
        if min_amount is not UNSET:
            field_dict["min_amount"] = min_amount
        if max_amount is not UNSET:
            field_dict["max_amount"] = max_amount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.charge_tier import ChargeTier

        d = dict(src_dict)
        unit_amount = d.pop("unit_amount", UNSET)

        package_amount = d.pop("package_amount", UNSET)

        package_size = d.pop("package_size", UNSET)

        _tiers = d.pop("tiers", UNSET)
        tiers: list[ChargeTier] | Unset = UNSET
        if _tiers is not UNSET:
            tiers = []
            for tiers_item_data in _tiers:
                tiers_item = ChargeTier.from_dict(tiers_item_data)

                tiers.append(tiers_item)

        rate = d.pop("rate", UNSET)

        fixed_amount = d.pop("fixed_amount", UNSET)

        free_units = d.pop("free_units", UNSET)

        min_amount = d.pop("min_amount", UNSET)

        max_amount = d.pop("max_amount", UNSET)

        charge_amounts = cls(
            unit_amount=unit_amount,
            package_amount=package_amount,
            package_size=package_size,
            tiers=tiers,
            rate=rate,
            fixed_amount=fixed_amount,
            free_units=free_units,
            min_amount=min_amount,
            max_amount=max_amount,
        )

        charge_amounts.additional_properties = d
        return charge_amounts

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
