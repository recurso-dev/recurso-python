from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="DunningTimingRate")



@_attrs_define
class DunningTimingRate:
    """ One time bucket's retry success rate.

        Attributes:
            bucket (int | Unset): Hour (0-23) or day-of-week (0-6, Sunday=0), UTC.
            total (int | Unset):
            successes (int | Unset):
            success_rate (float | Unset):
     """

    bucket: int | Unset = UNSET
    total: int | Unset = UNSET
    successes: int | Unset = UNSET
    success_rate: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        bucket = self.bucket

        total = self.total

        successes = self.successes

        success_rate = self.success_rate


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if bucket is not UNSET:
            field_dict["bucket"] = bucket
        if total is not UNSET:
            field_dict["total"] = total
        if successes is not UNSET:
            field_dict["successes"] = successes
        if success_rate is not UNSET:
            field_dict["success_rate"] = success_rate

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bucket = d.pop("bucket", UNSET)

        total = d.pop("total", UNSET)

        successes = d.pop("successes", UNSET)

        success_rate = d.pop("success_rate", UNSET)

        dunning_timing_rate = cls(
            bucket=bucket,
            total=total,
            successes=successes,
            success_rate=success_rate,
        )


        dunning_timing_rate.additional_properties = d
        return dunning_timing_rate

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
