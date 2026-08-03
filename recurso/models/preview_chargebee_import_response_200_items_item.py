from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.preview_chargebee_import_response_200_items_item_action import (
    PreviewChargebeeImportResponse200ItemsItemAction,
)
from ..models.preview_chargebee_import_response_200_items_item_kind import (
    PreviewChargebeeImportResponse200ItemsItemKind,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PreviewChargebeeImportResponse200ItemsItem")


@_attrs_define
class PreviewChargebeeImportResponse200ItemsItem:
    """
    Attributes:
        kind (PreviewChargebeeImportResponse200ItemsItemKind | Unset):
        chargebee_id (str | Unset):
        label (str | Unset):
        action (PreviewChargebeeImportResponse200ItemsItemAction | Unset):
        detail (str | Unset):
    """

    kind: PreviewChargebeeImportResponse200ItemsItemKind | Unset = UNSET
    chargebee_id: str | Unset = UNSET
    label: str | Unset = UNSET
    action: PreviewChargebeeImportResponse200ItemsItemAction | Unset = UNSET
    detail: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        chargebee_id = self.chargebee_id

        label = self.label

        action: str | Unset = UNSET
        if not isinstance(self.action, Unset):
            action = self.action.value

        detail = self.detail

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if kind is not UNSET:
            field_dict["kind"] = kind
        if chargebee_id is not UNSET:
            field_dict["chargebee_id"] = chargebee_id
        if label is not UNSET:
            field_dict["label"] = label
        if action is not UNSET:
            field_dict["action"] = action
        if detail is not UNSET:
            field_dict["detail"] = detail

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _kind = d.pop("kind", UNSET)
        kind: PreviewChargebeeImportResponse200ItemsItemKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = PreviewChargebeeImportResponse200ItemsItemKind(_kind)

        chargebee_id = d.pop("chargebee_id", UNSET)

        label = d.pop("label", UNSET)

        _action = d.pop("action", UNSET)
        action: PreviewChargebeeImportResponse200ItemsItemAction | Unset
        if isinstance(_action, Unset):
            action = UNSET
        else:
            action = PreviewChargebeeImportResponse200ItemsItemAction(_action)

        detail = d.pop("detail", UNSET)

        preview_chargebee_import_response_200_items_item = cls(
            kind=kind,
            chargebee_id=chargebee_id,
            label=label,
            action=action,
            detail=detail,
        )

        preview_chargebee_import_response_200_items_item.additional_properties = d
        return preview_chargebee_import_response_200_items_item

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
