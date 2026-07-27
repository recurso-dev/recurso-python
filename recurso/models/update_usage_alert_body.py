from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.update_usage_alert_body_threshold_type import UpdateUsageAlertBodyThresholdType






T = TypeVar("T", bound="UpdateUsageAlertBody")



@_attrs_define
class UpdateUsageAlertBody:
    """ 
        Attributes:
            threshold_type (UpdateUsageAlertBodyThresholdType):
            threshold (int):
     """

    threshold_type: UpdateUsageAlertBodyThresholdType
    threshold: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        threshold_type = self.threshold_type.value

        threshold = self.threshold


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "threshold_type": threshold_type,
            "threshold": threshold,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        threshold_type = UpdateUsageAlertBodyThresholdType(d.pop("threshold_type"))




        threshold = d.pop("threshold")

        update_usage_alert_body = cls(
            threshold_type=threshold_type,
            threshold=threshold,
        )


        update_usage_alert_body.additional_properties = d
        return update_usage_alert_body

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
