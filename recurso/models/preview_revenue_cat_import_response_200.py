from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.preview_revenue_cat_import_response_200_items_item import PreviewRevenueCatImportResponse200ItemsItem
    from ..models.preview_revenue_cat_import_response_200_summary import PreviewRevenueCatImportResponse200Summary


T = TypeVar("T", bound="PreviewRevenueCatImportResponse200")


@_attrs_define
class PreviewRevenueCatImportResponse200:
    """
    Attributes:
        items (list[PreviewRevenueCatImportResponse200ItemsItem] | Unset):
        summary (PreviewRevenueCatImportResponse200Summary | Unset):
        warnings (list[str] | Unset):
    """

    items: list[PreviewRevenueCatImportResponse200ItemsItem] | Unset = UNSET
    summary: PreviewRevenueCatImportResponse200Summary | Unset = UNSET
    warnings: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        summary: dict[str, Any] | Unset = UNSET
        if not isinstance(self.summary, Unset):
            summary = self.summary.to_dict()

        warnings: list[str] | Unset = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = self.warnings

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if items is not UNSET:
            field_dict["items"] = items
        if summary is not UNSET:
            field_dict["summary"] = summary
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.preview_revenue_cat_import_response_200_items_item import (
            PreviewRevenueCatImportResponse200ItemsItem,
        )
        from ..models.preview_revenue_cat_import_response_200_summary import PreviewRevenueCatImportResponse200Summary

        d = dict(src_dict)
        _items = d.pop("items", UNSET)
        items: list[PreviewRevenueCatImportResponse200ItemsItem] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = PreviewRevenueCatImportResponse200ItemsItem.from_dict(items_item_data)

                items.append(items_item)

        _summary = d.pop("summary", UNSET)
        summary: PreviewRevenueCatImportResponse200Summary | Unset
        if isinstance(_summary, Unset):
            summary = UNSET
        else:
            summary = PreviewRevenueCatImportResponse200Summary.from_dict(_summary)

        warnings = cast(list[str], d.pop("warnings", UNSET))

        preview_revenue_cat_import_response_200 = cls(
            items=items,
            summary=summary,
            warnings=warnings,
        )

        preview_revenue_cat_import_response_200.additional_properties = d
        return preview_revenue_cat_import_response_200

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
