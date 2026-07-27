from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CollectionsFailureBucket")


@_attrs_define
class CollectionsFailureBucket:
    """One failure reason ranked by money at risk.

    Attributes:
        error_code (str | Unset):
        count (int | Unset):
        amount_at_risk (int | Unset): Minor units at risk, FX-normalized to the reporting currency.
    """

    error_code: str | Unset = UNSET
    count: int | Unset = UNSET
    amount_at_risk: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error_code = self.error_code

        count = self.count

        amount_at_risk = self.amount_at_risk

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error_code is not UNSET:
            field_dict["error_code"] = error_code
        if count is not UNSET:
            field_dict["count"] = count
        if amount_at_risk is not UNSET:
            field_dict["amount_at_risk"] = amount_at_risk

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        error_code = d.pop("error_code", UNSET)

        count = d.pop("count", UNSET)

        amount_at_risk = d.pop("amount_at_risk", UNSET)

        collections_failure_bucket = cls(
            error_code=error_code,
            count=count,
            amount_at_risk=amount_at_risk,
        )

        collections_failure_bucket.additional_properties = d
        return collections_failure_bucket

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
