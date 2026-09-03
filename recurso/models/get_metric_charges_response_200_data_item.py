from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetMetricChargesResponse200DataItem")


@_attrs_define
class GetMetricChargesResponse200DataItem:
    """
    Attributes:
        charge_id (UUID | Unset):
        plan_id (UUID | Unset):
        plan_name (str | Unset):
        plan_code (str | Unset):
        plan_active (bool | Unset):
        charge_model (str | Unset):
        pay_in_advance (bool | Unset):
    """

    charge_id: UUID | Unset = UNSET
    plan_id: UUID | Unset = UNSET
    plan_name: str | Unset = UNSET
    plan_code: str | Unset = UNSET
    plan_active: bool | Unset = UNSET
    charge_model: str | Unset = UNSET
    pay_in_advance: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        charge_id: str | Unset = UNSET
        if not isinstance(self.charge_id, Unset):
            charge_id = str(self.charge_id)

        plan_id: str | Unset = UNSET
        if not isinstance(self.plan_id, Unset):
            plan_id = str(self.plan_id)

        plan_name = self.plan_name

        plan_code = self.plan_code

        plan_active = self.plan_active

        charge_model = self.charge_model

        pay_in_advance = self.pay_in_advance

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if charge_id is not UNSET:
            field_dict["charge_id"] = charge_id
        if plan_id is not UNSET:
            field_dict["plan_id"] = plan_id
        if plan_name is not UNSET:
            field_dict["plan_name"] = plan_name
        if plan_code is not UNSET:
            field_dict["plan_code"] = plan_code
        if plan_active is not UNSET:
            field_dict["plan_active"] = plan_active
        if charge_model is not UNSET:
            field_dict["charge_model"] = charge_model
        if pay_in_advance is not UNSET:
            field_dict["pay_in_advance"] = pay_in_advance

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _charge_id = d.pop("charge_id", UNSET)
        charge_id: UUID | Unset
        if isinstance(_charge_id, Unset):
            charge_id = UNSET
        else:
            charge_id = UUID(_charge_id)

        _plan_id = d.pop("plan_id", UNSET)
        plan_id: UUID | Unset
        if isinstance(_plan_id, Unset):
            plan_id = UNSET
        else:
            plan_id = UUID(_plan_id)

        plan_name = d.pop("plan_name", UNSET)

        plan_code = d.pop("plan_code", UNSET)

        plan_active = d.pop("plan_active", UNSET)

        charge_model = d.pop("charge_model", UNSET)

        pay_in_advance = d.pop("pay_in_advance", UNSET)

        get_metric_charges_response_200_data_item = cls(
            charge_id=charge_id,
            plan_id=plan_id,
            plan_name=plan_name,
            plan_code=plan_code,
            plan_active=plan_active,
            charge_model=charge_model,
            pay_in_advance=pay_in_advance,
        )

        get_metric_charges_response_200_data_item.additional_properties = d
        return get_metric_charges_response_200_data_item

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
