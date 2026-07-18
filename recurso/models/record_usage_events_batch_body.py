from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.record_usage_events_batch_body_events_item import RecordUsageEventsBatchBodyEventsItem


T = TypeVar("T", bound="RecordUsageEventsBatchBody")


@_attrs_define
class RecordUsageEventsBatchBody:
    """
    Attributes:
        events (list[RecordUsageEventsBatchBodyEventsItem]):
    """

    events: list[RecordUsageEventsBatchBodyEventsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        events = []
        for events_item_data in self.events:
            events_item = events_item_data.to_dict()
            events.append(events_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "events": events,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.record_usage_events_batch_body_events_item import RecordUsageEventsBatchBodyEventsItem

        d = dict(src_dict)
        events = []
        _events = d.pop("events")
        for events_item_data in _events:
            events_item = RecordUsageEventsBatchBodyEventsItem.from_dict(events_item_data)

            events.append(events_item)

        record_usage_events_batch_body = cls(
            events=events,
        )

        record_usage_events_batch_body.additional_properties = d
        return record_usage_events_batch_body

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
