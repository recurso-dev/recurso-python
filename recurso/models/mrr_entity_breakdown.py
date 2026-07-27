from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MRREntityBreakdown")


@_attrs_define
class MRREntityBreakdown:
    """One legal entity's MRR contribution, in the reporting currency.

    Attributes:
        entity_id (UUID | Unset):
        entity_name (str | Unset):
        is_primary (bool | Unset):
        normalized_mrr (int | Unset):
        arr (int | Unset):
        subscriptions (int | Unset):
    """

    entity_id: UUID | Unset = UNSET
    entity_name: str | Unset = UNSET
    is_primary: bool | Unset = UNSET
    normalized_mrr: int | Unset = UNSET
    arr: int | Unset = UNSET
    subscriptions: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entity_id: str | Unset = UNSET
        if not isinstance(self.entity_id, Unset):
            entity_id = str(self.entity_id)

        entity_name = self.entity_name

        is_primary = self.is_primary

        normalized_mrr = self.normalized_mrr

        arr = self.arr

        subscriptions = self.subscriptions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entity_id is not UNSET:
            field_dict["entity_id"] = entity_id
        if entity_name is not UNSET:
            field_dict["entity_name"] = entity_name
        if is_primary is not UNSET:
            field_dict["is_primary"] = is_primary
        if normalized_mrr is not UNSET:
            field_dict["normalized_mrr"] = normalized_mrr
        if arr is not UNSET:
            field_dict["arr"] = arr
        if subscriptions is not UNSET:
            field_dict["subscriptions"] = subscriptions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _entity_id = d.pop("entity_id", UNSET)
        entity_id: UUID | Unset
        if isinstance(_entity_id, Unset):
            entity_id = UNSET
        else:
            entity_id = UUID(_entity_id)

        entity_name = d.pop("entity_name", UNSET)

        is_primary = d.pop("is_primary", UNSET)

        normalized_mrr = d.pop("normalized_mrr", UNSET)

        arr = d.pop("arr", UNSET)

        subscriptions = d.pop("subscriptions", UNSET)

        mrr_entity_breakdown = cls(
            entity_id=entity_id,
            entity_name=entity_name,
            is_primary=is_primary,
            normalized_mrr=normalized_mrr,
            arr=arr,
            subscriptions=subscriptions,
        )

        mrr_entity_breakdown.additional_properties = d
        return mrr_entity_breakdown

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
