from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetSubscriptionFinancialSummaryResponse200DataOutstandingItem")


@_attrs_define
class GetSubscriptionFinancialSummaryResponse200DataOutstandingItem:
    """
    Attributes:
        currency (str | Unset):
        outstanding (int | Unset):
        past_due (int | Unset):
        past_due_count (int | Unset):
        billed (int | Unset):
        paid (int | Unset):
    """

    currency: str | Unset = UNSET
    outstanding: int | Unset = UNSET
    past_due: int | Unset = UNSET
    past_due_count: int | Unset = UNSET
    billed: int | Unset = UNSET
    paid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        currency = self.currency

        outstanding = self.outstanding

        past_due = self.past_due

        past_due_count = self.past_due_count

        billed = self.billed

        paid = self.paid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if currency is not UNSET:
            field_dict["currency"] = currency
        if outstanding is not UNSET:
            field_dict["outstanding"] = outstanding
        if past_due is not UNSET:
            field_dict["past_due"] = past_due
        if past_due_count is not UNSET:
            field_dict["past_due_count"] = past_due_count
        if billed is not UNSET:
            field_dict["billed"] = billed
        if paid is not UNSET:
            field_dict["paid"] = paid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        currency = d.pop("currency", UNSET)

        outstanding = d.pop("outstanding", UNSET)

        past_due = d.pop("past_due", UNSET)

        past_due_count = d.pop("past_due_count", UNSET)

        billed = d.pop("billed", UNSET)

        paid = d.pop("paid", UNSET)

        get_subscription_financial_summary_response_200_data_outstanding_item = cls(
            currency=currency,
            outstanding=outstanding,
            past_due=past_due,
            past_due_count=past_due_count,
            billed=billed,
            paid=paid,
        )

        get_subscription_financial_summary_response_200_data_outstanding_item.additional_properties = d
        return get_subscription_financial_summary_response_200_data_outstanding_item

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
