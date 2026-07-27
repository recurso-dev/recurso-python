from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.handle_go_cardless_webhook_for_connection_response_200_status import (
    HandleGoCardlessWebhookForConnectionResponse200Status,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="HandleGoCardlessWebhookForConnectionResponse200")


@_attrs_define
class HandleGoCardlessWebhookForConnectionResponse200:
    """
    Attributes:
        status (HandleGoCardlessWebhookForConnectionResponse200Status | Unset):
        processed (int | Unset):
    """

    status: HandleGoCardlessWebhookForConnectionResponse200Status | Unset = UNSET
    processed: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        processed = self.processed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if processed is not UNSET:
            field_dict["processed"] = processed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _status = d.pop("status", UNSET)
        status: HandleGoCardlessWebhookForConnectionResponse200Status | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = HandleGoCardlessWebhookForConnectionResponse200Status(_status)

        processed = d.pop("processed", UNSET)

        handle_go_cardless_webhook_for_connection_response_200 = cls(
            status=status,
            processed=processed,
        )

        handle_go_cardless_webhook_for_connection_response_200.additional_properties = d
        return handle_go_cardless_webhook_for_connection_response_200

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
