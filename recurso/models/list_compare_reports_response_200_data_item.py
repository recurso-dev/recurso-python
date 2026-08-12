from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListCompareReportsResponse200DataItem")


@_attrs_define
class ListCompareReportsResponse200DataItem:
    """
    Attributes:
        id (UUID | Unset):
        source (str | Unset):
        ready (bool | Unset):
        generated_at (datetime.datetime | Unset):
    """

    id: UUID | Unset = UNSET
    source: str | Unset = UNSET
    ready: bool | Unset = UNSET
    generated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        source = self.source

        ready = self.ready

        generated_at: str | Unset = UNSET
        if not isinstance(self.generated_at, Unset):
            generated_at = self.generated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if source is not UNSET:
            field_dict["source"] = source
        if ready is not UNSET:
            field_dict["ready"] = ready
        if generated_at is not UNSET:
            field_dict["generated_at"] = generated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        source = d.pop("source", UNSET)

        ready = d.pop("ready", UNSET)

        _generated_at = d.pop("generated_at", UNSET)
        generated_at: datetime.datetime | Unset
        if isinstance(_generated_at, Unset):
            generated_at = UNSET
        else:
            generated_at = datetime.datetime.fromisoformat(_generated_at)

        list_compare_reports_response_200_data_item = cls(
            id=id,
            source=source,
            ready=ready,
            generated_at=generated_at,
        )

        list_compare_reports_response_200_data_item.additional_properties = d
        return list_compare_reports_response_200_data_item

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
