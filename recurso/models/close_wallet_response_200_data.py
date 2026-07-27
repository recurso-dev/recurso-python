from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CloseWalletResponse200Data")


@_attrs_define
class CloseWalletResponse200Data:
    """
    Attributes:
        refunded (int | Unset): Paid balance to return (minor units)
        forfeited (int | Unset): Promotional balance written off (minor units)
    """

    refunded: int | Unset = UNSET
    forfeited: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        refunded = self.refunded

        forfeited = self.forfeited

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if refunded is not UNSET:
            field_dict["refunded"] = refunded
        if forfeited is not UNSET:
            field_dict["forfeited"] = forfeited

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        refunded = d.pop("refunded", UNSET)

        forfeited = d.pop("forfeited", UNSET)

        close_wallet_response_200_data = cls(
            refunded=refunded,
            forfeited=forfeited,
        )

        close_wallet_response_200_data.additional_properties = d
        return close_wallet_response_200_data

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
