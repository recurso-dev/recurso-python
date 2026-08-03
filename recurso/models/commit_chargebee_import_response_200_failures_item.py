from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CommitChargebeeImportResponse200FailuresItem")


@_attrs_define
class CommitChargebeeImportResponse200FailuresItem:
    """
    Attributes:
        kind (str | Unset):
        stripe_id (str | Unset):
        error (str | Unset):
    """

    kind: str | Unset = UNSET
    stripe_id: str | Unset = UNSET
    error: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind

        stripe_id = self.stripe_id

        error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if kind is not UNSET:
            field_dict["kind"] = kind
        if stripe_id is not UNSET:
            field_dict["stripe_id"] = stripe_id
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = d.pop("kind", UNSET)

        stripe_id = d.pop("stripe_id", UNSET)

        error = d.pop("error", UNSET)

        commit_chargebee_import_response_200_failures_item = cls(
            kind=kind,
            stripe_id=stripe_id,
            error=error,
        )

        commit_chargebee_import_response_200_failures_item.additional_properties = d
        return commit_chargebee_import_response_200_failures_item

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
