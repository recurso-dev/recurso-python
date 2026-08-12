from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CompareRevenueCatImportResponse200IssuesItem")


@_attrs_define
class CompareRevenueCatImportResponse200IssuesItem:
    """
    Attributes:
        kind (str | Unset):
        external_id (str | Unset):
        field (str | Unset):
        source (str | Unset):
        recurso (str | Unset):
    """

    kind: str | Unset = UNSET
    external_id: str | Unset = UNSET
    field: str | Unset = UNSET
    source: str | Unset = UNSET
    recurso: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind

        external_id = self.external_id

        field = self.field

        source = self.source

        recurso = self.recurso

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if kind is not UNSET:
            field_dict["kind"] = kind
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if field is not UNSET:
            field_dict["field"] = field
        if source is not UNSET:
            field_dict["source"] = source
        if recurso is not UNSET:
            field_dict["recurso"] = recurso

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = d.pop("kind", UNSET)

        external_id = d.pop("external_id", UNSET)

        field = d.pop("field", UNSET)

        source = d.pop("source", UNSET)

        recurso = d.pop("recurso", UNSET)

        compare_revenue_cat_import_response_200_issues_item = cls(
            kind=kind,
            external_id=external_id,
            field=field,
            source=source,
            recurso=recurso,
        )

        compare_revenue_cat_import_response_200_issues_item.additional_properties = d
        return compare_revenue_cat_import_response_200_issues_item

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
