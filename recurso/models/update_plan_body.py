from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_plan_body_interval_unit import UpdatePlanBodyIntervalUnit
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdatePlanBody")


@_attrs_define
class UpdatePlanBody:
    """
    Attributes:
        name (str | Unset):
        hsn_code (str | Unset):
        interval_unit (UpdatePlanBodyIntervalUnit | Unset):
        interval_count (int | Unset):
        active (bool | Unset):
    """

    name: str | Unset = UNSET
    hsn_code: str | Unset = UNSET
    interval_unit: UpdatePlanBodyIntervalUnit | Unset = UNSET
    interval_count: int | Unset = UNSET
    active: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        hsn_code = self.hsn_code

        interval_unit: str | Unset = UNSET
        if not isinstance(self.interval_unit, Unset):
            interval_unit = self.interval_unit.value

        interval_count = self.interval_count

        active = self.active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if hsn_code is not UNSET:
            field_dict["hsn_code"] = hsn_code
        if interval_unit is not UNSET:
            field_dict["interval_unit"] = interval_unit
        if interval_count is not UNSET:
            field_dict["interval_count"] = interval_count
        if active is not UNSET:
            field_dict["active"] = active

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        hsn_code = d.pop("hsn_code", UNSET)

        _interval_unit = d.pop("interval_unit", UNSET)
        interval_unit: UpdatePlanBodyIntervalUnit | Unset
        if isinstance(_interval_unit, Unset):
            interval_unit = UNSET
        else:
            interval_unit = UpdatePlanBodyIntervalUnit(_interval_unit)

        interval_count = d.pop("interval_count", UNSET)

        active = d.pop("active", UNSET)

        update_plan_body = cls(
            name=name,
            hsn_code=hsn_code,
            interval_unit=interval_unit,
            interval_count=interval_count,
            active=active,
        )

        update_plan_body.additional_properties = d
        return update_plan_body

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
