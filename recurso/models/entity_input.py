from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EntityInput")


@_attrs_define
class EntityInput:
    """
    Attributes:
        name (str):
        legal_name (str | Unset):
        invoice_prefix (str | Unset): Optional; defaults to a slug of the name.
        country_code (str | Unset):
    """

    name: str
    legal_name: str | Unset = UNSET
    invoice_prefix: str | Unset = UNSET
    country_code: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        legal_name = self.legal_name

        invoice_prefix = self.invoice_prefix

        country_code = self.country_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if legal_name is not UNSET:
            field_dict["legal_name"] = legal_name
        if invoice_prefix is not UNSET:
            field_dict["invoice_prefix"] = invoice_prefix
        if country_code is not UNSET:
            field_dict["country_code"] = country_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        legal_name = d.pop("legal_name", UNSET)

        invoice_prefix = d.pop("invoice_prefix", UNSET)

        country_code = d.pop("country_code", UNSET)

        entity_input = cls(
            name=name,
            legal_name=legal_name,
            invoice_prefix=invoice_prefix,
            country_code=country_code,
        )

        entity_input.additional_properties = d
        return entity_input

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
