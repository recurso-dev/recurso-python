from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InvoiceBranding")


@_attrs_define
class InvoiceBranding:
    """A tenant's invoice presentation settings — display name, logo, signature, signatory, bank details and terms rendered
    on invoice documents. Presentation only; statutory seller identity (GST / W-9) takes precedence on tax invoices.

        Attributes:
            company_name (str | Unset): Display name shown at the top of invoices (max 200 chars).
            logo_data_url (str | Unset): Logo as a data:image/png or data:image/jpeg base64 URL (max 300KB decoded).
            signature_data_url (str | Unset): Signature image as a data:image/png or data:image/jpeg base64 URL (max 300KB
                decoded).
            signatory_name (str | Unset): Name printed under the signature line (max 200 chars).
            bank_details (str | Unset): Bank/remittance details shown in the invoice footer (max 4000 chars).
            terms (str | Unset): Terms and conditions shown in the invoice footer (max 4000 chars).
    """

    company_name: str | Unset = UNSET
    logo_data_url: str | Unset = UNSET
    signature_data_url: str | Unset = UNSET
    signatory_name: str | Unset = UNSET
    bank_details: str | Unset = UNSET
    terms: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company_name = self.company_name

        logo_data_url = self.logo_data_url

        signature_data_url = self.signature_data_url

        signatory_name = self.signatory_name

        bank_details = self.bank_details

        terms = self.terms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if company_name is not UNSET:
            field_dict["company_name"] = company_name
        if logo_data_url is not UNSET:
            field_dict["logo_data_url"] = logo_data_url
        if signature_data_url is not UNSET:
            field_dict["signature_data_url"] = signature_data_url
        if signatory_name is not UNSET:
            field_dict["signatory_name"] = signatory_name
        if bank_details is not UNSET:
            field_dict["bank_details"] = bank_details
        if terms is not UNSET:
            field_dict["terms"] = terms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        company_name = d.pop("company_name", UNSET)

        logo_data_url = d.pop("logo_data_url", UNSET)

        signature_data_url = d.pop("signature_data_url", UNSET)

        signatory_name = d.pop("signatory_name", UNSET)

        bank_details = d.pop("bank_details", UNSET)

        terms = d.pop("terms", UNSET)

        invoice_branding = cls(
            company_name=company_name,
            logo_data_url=logo_data_url,
            signature_data_url=signature_data_url,
            signatory_name=signatory_name,
            bank_details=bank_details,
            terms=terms,
        )

        invoice_branding.additional_properties = d
        return invoice_branding

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
