from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_customer_financial_summary_response_200_data_currencies_item import (
        GetCustomerFinancialSummaryResponse200DataCurrenciesItem,
    )


T = TypeVar("T", bound="GetCustomerFinancialSummaryResponse200Data")


@_attrs_define
class GetCustomerFinancialSummaryResponse200Data:
    """
    Attributes:
        customer_id (UUID | Unset):
        currencies (list[GetCustomerFinancialSummaryResponse200DataCurrenciesItem] | Unset):
    """

    customer_id: UUID | Unset = UNSET
    currencies: list[GetCustomerFinancialSummaryResponse200DataCurrenciesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        customer_id: str | Unset = UNSET
        if not isinstance(self.customer_id, Unset):
            customer_id = str(self.customer_id)

        currencies: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.currencies, Unset):
            currencies = []
            for currencies_item_data in self.currencies:
                currencies_item = currencies_item_data.to_dict()
                currencies.append(currencies_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if customer_id is not UNSET:
            field_dict["customer_id"] = customer_id
        if currencies is not UNSET:
            field_dict["currencies"] = currencies

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_customer_financial_summary_response_200_data_currencies_item import (
            GetCustomerFinancialSummaryResponse200DataCurrenciesItem,
        )

        d = dict(src_dict)
        _customer_id = d.pop("customer_id", UNSET)
        customer_id: UUID | Unset
        if isinstance(_customer_id, Unset):
            customer_id = UNSET
        else:
            customer_id = UUID(_customer_id)

        _currencies = d.pop("currencies", UNSET)
        currencies: list[GetCustomerFinancialSummaryResponse200DataCurrenciesItem] | Unset = UNSET
        if _currencies is not UNSET:
            currencies = []
            for currencies_item_data in _currencies:
                currencies_item = GetCustomerFinancialSummaryResponse200DataCurrenciesItem.from_dict(
                    currencies_item_data
                )

                currencies.append(currencies_item)

        get_customer_financial_summary_response_200_data = cls(
            customer_id=customer_id,
            currencies=currencies,
        )

        get_customer_financial_summary_response_200_data.additional_properties = d
        return get_customer_financial_summary_response_200_data

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
