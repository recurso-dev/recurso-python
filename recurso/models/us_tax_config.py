from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="USTaxConfig")


@_attrs_define
class USTaxConfig:
    """A tenant's US tax identity (W-9) — the seller party shown on US sales-tax invoices. Presentation only.

    Attributes:
        legal_name (str | Unset): Seller legal name shown on US invoices.
        ein (str | Unset): Employer Identification Number (the W-9 tax id).
        address (str | Unset): Seller postal address shown on US invoices.
    """

    legal_name: str | Unset = UNSET
    ein: str | Unset = UNSET
    address: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        legal_name = self.legal_name

        ein = self.ein

        address = self.address

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if legal_name is not UNSET:
            field_dict["legal_name"] = legal_name
        if ein is not UNSET:
            field_dict["ein"] = ein
        if address is not UNSET:
            field_dict["address"] = address

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        legal_name = d.pop("legal_name", UNSET)

        ein = d.pop("ein", UNSET)

        address = d.pop("address", UNSET)

        us_tax_config = cls(
            legal_name=legal_name,
            ein=ein,
            address=address,
        )

        us_tax_config.additional_properties = d
        return us_tax_config

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
