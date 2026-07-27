from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from uuid import UUID






T = TypeVar("T", bound="SimulateChargesBodyUsageItem")



@_attrs_define
class SimulateChargesBodyUsageItem:
    """ 
        Attributes:
            metric_id (UUID | Unset):
            quantity (int | Unset):
     """

    metric_id: UUID | Unset = UNSET
    quantity: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        metric_id: str | Unset = UNSET
        if not isinstance(self.metric_id, Unset):
            metric_id = str(self.metric_id)

        quantity = self.quantity


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if metric_id is not UNSET:
            field_dict["metric_id"] = metric_id
        if quantity is not UNSET:
            field_dict["quantity"] = quantity

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _metric_id = d.pop("metric_id", UNSET)
        metric_id: UUID | Unset
        if isinstance(_metric_id,  Unset):
            metric_id = UNSET
        else:
            metric_id = UUID(_metric_id)




        quantity = d.pop("quantity", UNSET)

        simulate_charges_body_usage_item = cls(
            metric_id=metric_id,
            quantity=quantity,
        )


        simulate_charges_body_usage_item.additional_properties = d
        return simulate_charges_body_usage_item

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
