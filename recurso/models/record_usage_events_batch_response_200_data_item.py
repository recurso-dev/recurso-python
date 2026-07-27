from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.record_usage_events_batch_response_200_data_item_status import (
    RecordUsageEventsBatchResponse200DataItemStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RecordUsageEventsBatchResponse200DataItem")


@_attrs_define
class RecordUsageEventsBatchResponse200DataItem:
    """
    Attributes:
        index (int | Unset):
        status (RecordUsageEventsBatchResponse200DataItemStatus | Unset):
        event_id (UUID | Unset):
        error (str | Unset):
    """

    index: int | Unset = UNSET
    status: RecordUsageEventsBatchResponse200DataItemStatus | Unset = UNSET
    event_id: UUID | Unset = UNSET
    error: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        index = self.index

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        event_id: str | Unset = UNSET
        if not isinstance(self.event_id, Unset):
            event_id = str(self.event_id)

        error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if index is not UNSET:
            field_dict["index"] = index
        if status is not UNSET:
            field_dict["status"] = status
        if event_id is not UNSET:
            field_dict["event_id"] = event_id
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        index = d.pop("index", UNSET)

        _status = d.pop("status", UNSET)
        status: RecordUsageEventsBatchResponse200DataItemStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = RecordUsageEventsBatchResponse200DataItemStatus(_status)

        _event_id = d.pop("event_id", UNSET)
        event_id: UUID | Unset
        if isinstance(_event_id, Unset):
            event_id = UNSET
        else:
            event_id = UUID(_event_id)

        error = d.pop("error", UNSET)

        record_usage_events_batch_response_200_data_item = cls(
            index=index,
            status=status,
            event_id=event_id,
            error=error,
        )

        record_usage_events_batch_response_200_data_item.additional_properties = d
        return record_usage_events_batch_response_200_data_item

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
