from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EntityOverviewRow")


@_attrs_define
class EntityOverviewRow:
    """One legal entity's MRR + open AR, in the reporting currency.

    Attributes:
        entity_id (UUID | Unset):
        entity_name (str | Unset):
        is_primary (bool | Unset):
        mrr (int | Unset):
        arr (int | Unset):
        ar_outstanding (int | Unset):
        subscriptions (int | Unset):
    """

    entity_id: UUID | Unset = UNSET
    entity_name: str | Unset = UNSET
    is_primary: bool | Unset = UNSET
    mrr: int | Unset = UNSET
    arr: int | Unset = UNSET
    ar_outstanding: int | Unset = UNSET
    subscriptions: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entity_id: str | Unset = UNSET
        if not isinstance(self.entity_id, Unset):
            entity_id = str(self.entity_id)

        entity_name = self.entity_name

        is_primary = self.is_primary

        mrr = self.mrr

        arr = self.arr

        ar_outstanding = self.ar_outstanding

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
        if mrr is not UNSET:
            field_dict["mrr"] = mrr
        if arr is not UNSET:
            field_dict["arr"] = arr
        if ar_outstanding is not UNSET:
            field_dict["ar_outstanding"] = ar_outstanding
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

        mrr = d.pop("mrr", UNSET)

        arr = d.pop("arr", UNSET)

        ar_outstanding = d.pop("ar_outstanding", UNSET)

        subscriptions = d.pop("subscriptions", UNSET)

        entity_overview_row = cls(
            entity_id=entity_id,
            entity_name=entity_name,
            is_primary=is_primary,
            mrr=mrr,
            arr=arr,
            ar_outstanding=ar_outstanding,
            subscriptions=subscriptions,
        )

        entity_overview_row.additional_properties = d
        return entity_overview_row

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
