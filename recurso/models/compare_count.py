from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CompareCount")


@_attrs_define
class CompareCount:
    """Migration-compare coverage for one record kind.

    Attributes:
        source (int | Unset): Importable records in the export.
        matched (int | Unset): Found in Recurso.
        missing (int | Unset):
    """

    source: int | Unset = UNSET
    matched: int | Unset = UNSET
    missing: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source = self.source

        matched = self.matched

        missing = self.missing

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if source is not UNSET:
            field_dict["source"] = source
        if matched is not UNSET:
            field_dict["matched"] = matched
        if missing is not UNSET:
            field_dict["missing"] = missing

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        source = d.pop("source", UNSET)

        matched = d.pop("matched", UNSET)

        missing = d.pop("missing", UNSET)

        compare_count = cls(
            source=source,
            matched=matched,
            missing=missing,
        )

        compare_count.additional_properties = d
        return compare_count

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
