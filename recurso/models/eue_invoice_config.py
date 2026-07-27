from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="EUEInvoiceConfig")



@_attrs_define
class EUEInvoiceConfig:
    """ A tenant's EU e-invoicing configuration — the opt-in flag plus the EN 16931 seller party.

        Attributes:
            enabled (bool | Unset): When true, invoices generate an EN 16931 (UBL 2.1) e-invoice. Off by default.
            legal_name (str | Unset): Seller registered/legal name (BT-27). Required to enable.
            vat_number (str | Unset): Seller VAT identifier incl. country prefix, e.g. "DE123456789" (BT-31). Required to
                enable.
            country_code (str | Unset): Seller country as an ISO 3166-1 alpha-2 code (BT-40). Required to enable.
            street (str | Unset):
            city (str | Unset):
            postal_zone (str | Unset):
     """

    enabled: bool | Unset = UNSET
    legal_name: str | Unset = UNSET
    vat_number: str | Unset = UNSET
    country_code: str | Unset = UNSET
    street: str | Unset = UNSET
    city: str | Unset = UNSET
    postal_zone: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        legal_name = self.legal_name

        vat_number = self.vat_number

        country_code = self.country_code

        street = self.street

        city = self.city

        postal_zone = self.postal_zone


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if legal_name is not UNSET:
            field_dict["legal_name"] = legal_name
        if vat_number is not UNSET:
            field_dict["vat_number"] = vat_number
        if country_code is not UNSET:
            field_dict["country_code"] = country_code
        if street is not UNSET:
            field_dict["street"] = street
        if city is not UNSET:
            field_dict["city"] = city
        if postal_zone is not UNSET:
            field_dict["postal_zone"] = postal_zone

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        legal_name = d.pop("legal_name", UNSET)

        vat_number = d.pop("vat_number", UNSET)

        country_code = d.pop("country_code", UNSET)

        street = d.pop("street", UNSET)

        city = d.pop("city", UNSET)

        postal_zone = d.pop("postal_zone", UNSET)

        eue_invoice_config = cls(
            enabled=enabled,
            legal_name=legal_name,
            vat_number=vat_number,
            country_code=country_code,
            street=street,
            city=city,
            postal_zone=postal_zone,
        )


        eue_invoice_config.additional_properties = d
        return eue_invoice_config

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
