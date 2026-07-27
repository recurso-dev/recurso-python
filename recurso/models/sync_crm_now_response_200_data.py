from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SyncCRMNowResponse200Data")


@_attrs_define
class SyncCRMNowResponse200Data:
    """
    Attributes:
        contacts_synced (int | Unset):
        contacts_remaining (int | Unset): Eligible contacts not pushed this call (manual sync is capped; the daily sweep
            finishes them).
    """

    contacts_synced: int | Unset = UNSET
    contacts_remaining: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        contacts_synced = self.contacts_synced

        contacts_remaining = self.contacts_remaining

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if contacts_synced is not UNSET:
            field_dict["contacts_synced"] = contacts_synced
        if contacts_remaining is not UNSET:
            field_dict["contacts_remaining"] = contacts_remaining

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        contacts_synced = d.pop("contacts_synced", UNSET)

        contacts_remaining = d.pop("contacts_remaining", UNSET)

        sync_crm_now_response_200_data = cls(
            contacts_synced=contacts_synced,
            contacts_remaining=contacts_remaining,
        )

        sync_crm_now_response_200_data.additional_properties = d
        return sync_crm_now_response_200_data

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
