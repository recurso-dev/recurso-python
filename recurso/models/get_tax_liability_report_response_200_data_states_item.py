from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_tax_liability_report_response_200_data_states_item_nexus_type import (
    GetTaxLiabilityReportResponse200DataStatesItemNexusType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetTaxLiabilityReportResponse200DataStatesItem")


@_attrs_define
class GetTaxLiabilityReportResponse200DataStatesItem:
    """
    Attributes:
        state_code (str | Unset):
        gross_sales (int | Unset):
        taxable_sales (int | Unset):
        exempt_sales (int | Unset):
        non_taxable_sales (int | Unset):
        tax_collected (int | Unset):
        invoice_count (int | Unset):
        has_nexus (bool | Unset):
        nexus_type (GetTaxLiabilityReportResponse200DataStatesItemNexusType | Unset):
    """

    state_code: str | Unset = UNSET
    gross_sales: int | Unset = UNSET
    taxable_sales: int | Unset = UNSET
    exempt_sales: int | Unset = UNSET
    non_taxable_sales: int | Unset = UNSET
    tax_collected: int | Unset = UNSET
    invoice_count: int | Unset = UNSET
    has_nexus: bool | Unset = UNSET
    nexus_type: GetTaxLiabilityReportResponse200DataStatesItemNexusType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        state_code = self.state_code

        gross_sales = self.gross_sales

        taxable_sales = self.taxable_sales

        exempt_sales = self.exempt_sales

        non_taxable_sales = self.non_taxable_sales

        tax_collected = self.tax_collected

        invoice_count = self.invoice_count

        has_nexus = self.has_nexus

        nexus_type: str | Unset = UNSET
        if not isinstance(self.nexus_type, Unset):
            nexus_type = self.nexus_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if state_code is not UNSET:
            field_dict["state_code"] = state_code
        if gross_sales is not UNSET:
            field_dict["gross_sales"] = gross_sales
        if taxable_sales is not UNSET:
            field_dict["taxable_sales"] = taxable_sales
        if exempt_sales is not UNSET:
            field_dict["exempt_sales"] = exempt_sales
        if non_taxable_sales is not UNSET:
            field_dict["non_taxable_sales"] = non_taxable_sales
        if tax_collected is not UNSET:
            field_dict["tax_collected"] = tax_collected
        if invoice_count is not UNSET:
            field_dict["invoice_count"] = invoice_count
        if has_nexus is not UNSET:
            field_dict["has_nexus"] = has_nexus
        if nexus_type is not UNSET:
            field_dict["nexus_type"] = nexus_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        state_code = d.pop("state_code", UNSET)

        gross_sales = d.pop("gross_sales", UNSET)

        taxable_sales = d.pop("taxable_sales", UNSET)

        exempt_sales = d.pop("exempt_sales", UNSET)

        non_taxable_sales = d.pop("non_taxable_sales", UNSET)

        tax_collected = d.pop("tax_collected", UNSET)

        invoice_count = d.pop("invoice_count", UNSET)

        has_nexus = d.pop("has_nexus", UNSET)

        _nexus_type = d.pop("nexus_type", UNSET)
        nexus_type: GetTaxLiabilityReportResponse200DataStatesItemNexusType | Unset
        if isinstance(_nexus_type, Unset):
            nexus_type = UNSET
        else:
            nexus_type = GetTaxLiabilityReportResponse200DataStatesItemNexusType(_nexus_type)

        get_tax_liability_report_response_200_data_states_item = cls(
            state_code=state_code,
            gross_sales=gross_sales,
            taxable_sales=taxable_sales,
            exempt_sales=exempt_sales,
            non_taxable_sales=non_taxable_sales,
            tax_collected=tax_collected,
            invoice_count=invoice_count,
            has_nexus=has_nexus,
            nexus_type=nexus_type,
        )

        get_tax_liability_report_response_200_data_states_item.additional_properties = d
        return get_tax_liability_report_response_200_data_states_item

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
