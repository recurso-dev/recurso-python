from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_tax_liability_report_response_200_data_states_item import (
        GetTaxLiabilityReportResponse200DataStatesItem,
    )


T = TypeVar("T", bound="GetTaxLiabilityReportResponse200Data")


@_attrs_define
class GetTaxLiabilityReportResponse200Data:
    """
    Attributes:
        from_date (datetime.date | Unset):
        to_date (datetime.date | Unset):
        currency (str | Unset):
        total_gross_sales (int | Unset):
        total_tax_collected (int | Unset):
        states (list[GetTaxLiabilityReportResponse200DataStatesItem] | Unset):
    """

    from_date: datetime.date | Unset = UNSET
    to_date: datetime.date | Unset = UNSET
    currency: str | Unset = UNSET
    total_gross_sales: int | Unset = UNSET
    total_tax_collected: int | Unset = UNSET
    states: list[GetTaxLiabilityReportResponse200DataStatesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_date: str | Unset = UNSET
        if not isinstance(self.from_date, Unset):
            from_date = self.from_date.isoformat()

        to_date: str | Unset = UNSET
        if not isinstance(self.to_date, Unset):
            to_date = self.to_date.isoformat()

        currency = self.currency

        total_gross_sales = self.total_gross_sales

        total_tax_collected = self.total_tax_collected

        states: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.states, Unset):
            states = []
            for states_item_data in self.states:
                states_item = states_item_data.to_dict()
                states.append(states_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if from_date is not UNSET:
            field_dict["from_date"] = from_date
        if to_date is not UNSET:
            field_dict["to_date"] = to_date
        if currency is not UNSET:
            field_dict["currency"] = currency
        if total_gross_sales is not UNSET:
            field_dict["total_gross_sales"] = total_gross_sales
        if total_tax_collected is not UNSET:
            field_dict["total_tax_collected"] = total_tax_collected
        if states is not UNSET:
            field_dict["states"] = states

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_tax_liability_report_response_200_data_states_item import (
            GetTaxLiabilityReportResponse200DataStatesItem,
        )

        d = dict(src_dict)
        _from_date = d.pop("from_date", UNSET)
        from_date: datetime.date | Unset
        if isinstance(_from_date, Unset):
            from_date = UNSET
        else:
            from_date = datetime.date.fromisoformat(_from_date)

        _to_date = d.pop("to_date", UNSET)
        to_date: datetime.date | Unset
        if isinstance(_to_date, Unset):
            to_date = UNSET
        else:
            to_date = datetime.date.fromisoformat(_to_date)

        currency = d.pop("currency", UNSET)

        total_gross_sales = d.pop("total_gross_sales", UNSET)

        total_tax_collected = d.pop("total_tax_collected", UNSET)

        _states = d.pop("states", UNSET)
        states: list[GetTaxLiabilityReportResponse200DataStatesItem] | Unset = UNSET
        if _states is not UNSET:
            states = []
            for states_item_data in _states:
                states_item = GetTaxLiabilityReportResponse200DataStatesItem.from_dict(states_item_data)

                states.append(states_item)

        get_tax_liability_report_response_200_data = cls(
            from_date=from_date,
            to_date=to_date,
            currency=currency,
            total_gross_sales=total_gross_sales,
            total_tax_collected=total_tax_collected,
            states=states,
        )

        get_tax_liability_report_response_200_data.additional_properties = d
        return get_tax_liability_report_response_200_data

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
