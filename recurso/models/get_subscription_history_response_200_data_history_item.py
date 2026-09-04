from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_subscription_history_response_200_data_history_item_change_type import (
    GetSubscriptionHistoryResponse200DataHistoryItemChangeType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetSubscriptionHistoryResponse200DataHistoryItem")


@_attrs_define
class GetSubscriptionHistoryResponse200DataHistoryItem:
    """
    Attributes:
        id (UUID | Unset):
        subscription_id (UUID | Unset):
        change_type (GetSubscriptionHistoryResponse200DataHistoryItemChangeType | Unset):
        from_value (None | str | Unset):
        to_value (None | str | Unset):
        changed_at (datetime.datetime | Unset):
    """

    id: UUID | Unset = UNSET
    subscription_id: UUID | Unset = UNSET
    change_type: GetSubscriptionHistoryResponse200DataHistoryItemChangeType | Unset = UNSET
    from_value: None | str | Unset = UNSET
    to_value: None | str | Unset = UNSET
    changed_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        subscription_id: str | Unset = UNSET
        if not isinstance(self.subscription_id, Unset):
            subscription_id = str(self.subscription_id)

        change_type: str | Unset = UNSET
        if not isinstance(self.change_type, Unset):
            change_type = self.change_type.value

        from_value: None | str | Unset
        if isinstance(self.from_value, Unset):
            from_value = UNSET
        else:
            from_value = self.from_value

        to_value: None | str | Unset
        if isinstance(self.to_value, Unset):
            to_value = UNSET
        else:
            to_value = self.to_value

        changed_at: str | Unset = UNSET
        if not isinstance(self.changed_at, Unset):
            changed_at = self.changed_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if subscription_id is not UNSET:
            field_dict["subscription_id"] = subscription_id
        if change_type is not UNSET:
            field_dict["change_type"] = change_type
        if from_value is not UNSET:
            field_dict["from_value"] = from_value
        if to_value is not UNSET:
            field_dict["to_value"] = to_value
        if changed_at is not UNSET:
            field_dict["changed_at"] = changed_at

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

        _subscription_id = d.pop("subscription_id", UNSET)
        subscription_id: UUID | Unset
        if isinstance(_subscription_id, Unset):
            subscription_id = UNSET
        else:
            subscription_id = UUID(_subscription_id)

        _change_type = d.pop("change_type", UNSET)
        change_type: GetSubscriptionHistoryResponse200DataHistoryItemChangeType | Unset
        if isinstance(_change_type, Unset):
            change_type = UNSET
        else:
            change_type = GetSubscriptionHistoryResponse200DataHistoryItemChangeType(_change_type)

        def _parse_from_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        from_value = _parse_from_value(d.pop("from_value", UNSET))

        def _parse_to_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        to_value = _parse_to_value(d.pop("to_value", UNSET))

        _changed_at = d.pop("changed_at", UNSET)
        changed_at: datetime.datetime | Unset
        if isinstance(_changed_at, Unset):
            changed_at = UNSET
        else:
            changed_at = datetime.datetime.fromisoformat(_changed_at)

        get_subscription_history_response_200_data_history_item = cls(
            id=id,
            subscription_id=subscription_id,
            change_type=change_type,
            from_value=from_value,
            to_value=to_value,
            changed_at=changed_at,
        )

        get_subscription_history_response_200_data_history_item.additional_properties = d
        return get_subscription_history_response_200_data_history_item

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
