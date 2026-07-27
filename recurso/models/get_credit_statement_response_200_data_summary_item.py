from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetCreditStatementResponse200DataSummaryItem")


@_attrs_define
class GetCreditStatementResponse200DataSummaryItem:
    """
    Attributes:
        currency (str | Unset):
        total_issued (int | Unset):
        total_applied (int | Unset):
        current_balance (int | Unset):
    """

    currency: str | Unset = UNSET
    total_issued: int | Unset = UNSET
    total_applied: int | Unset = UNSET
    current_balance: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        currency = self.currency

        total_issued = self.total_issued

        total_applied = self.total_applied

        current_balance = self.current_balance

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if currency is not UNSET:
            field_dict["currency"] = currency
        if total_issued is not UNSET:
            field_dict["total_issued"] = total_issued
        if total_applied is not UNSET:
            field_dict["total_applied"] = total_applied
        if current_balance is not UNSET:
            field_dict["current_balance"] = current_balance

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        currency = d.pop("currency", UNSET)

        total_issued = d.pop("total_issued", UNSET)

        total_applied = d.pop("total_applied", UNSET)

        current_balance = d.pop("current_balance", UNSET)

        get_credit_statement_response_200_data_summary_item = cls(
            currency=currency,
            total_issued=total_issued,
            total_applied=total_applied,
            current_balance=current_balance,
        )

        get_credit_statement_response_200_data_summary_item.additional_properties = d
        return get_credit_statement_response_200_data_summary_item

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
