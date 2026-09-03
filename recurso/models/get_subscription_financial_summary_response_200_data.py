from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_subscription_financial_summary_response_200_data_outstanding_item import (
        GetSubscriptionFinancialSummaryResponse200DataOutstandingItem,
    )


T = TypeVar("T", bound="GetSubscriptionFinancialSummaryResponse200Data")


@_attrs_define
class GetSubscriptionFinancialSummaryResponse200Data:
    """
    Attributes:
        subscription_id (UUID | Unset):
        status (str | Unset):
        currency (str | Unset):
        mrr (int | Unset): Monthly-normalized recurring value; 0 unless active.
        recurring_amount (int | Unset):
        interval_unit (str | Unset):
        interval_count (int | Unset):
        current_period_start (datetime.datetime | Unset):
        current_period_end (datetime.datetime | Unset):
        next_invoice_date (datetime.datetime | None | Unset):
        next_invoice_base_amount (int | Unset): Plan list price only; excludes tax/coupon/add-ons/usage. Never the total
            due.
        coupon_id (None | Unset | UUID):
        discount_active (bool | Unset):
        outstanding (list[GetSubscriptionFinancialSummaryResponse200DataOutstandingItem] | Unset):
    """

    subscription_id: UUID | Unset = UNSET
    status: str | Unset = UNSET
    currency: str | Unset = UNSET
    mrr: int | Unset = UNSET
    recurring_amount: int | Unset = UNSET
    interval_unit: str | Unset = UNSET
    interval_count: int | Unset = UNSET
    current_period_start: datetime.datetime | Unset = UNSET
    current_period_end: datetime.datetime | Unset = UNSET
    next_invoice_date: datetime.datetime | None | Unset = UNSET
    next_invoice_base_amount: int | Unset = UNSET
    coupon_id: None | Unset | UUID = UNSET
    discount_active: bool | Unset = UNSET
    outstanding: list[GetSubscriptionFinancialSummaryResponse200DataOutstandingItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        subscription_id: str | Unset = UNSET
        if not isinstance(self.subscription_id, Unset):
            subscription_id = str(self.subscription_id)

        status = self.status

        currency = self.currency

        mrr = self.mrr

        recurring_amount = self.recurring_amount

        interval_unit = self.interval_unit

        interval_count = self.interval_count

        current_period_start: str | Unset = UNSET
        if not isinstance(self.current_period_start, Unset):
            current_period_start = self.current_period_start.isoformat()

        current_period_end: str | Unset = UNSET
        if not isinstance(self.current_period_end, Unset):
            current_period_end = self.current_period_end.isoformat()

        next_invoice_date: None | str | Unset
        if isinstance(self.next_invoice_date, Unset):
            next_invoice_date = UNSET
        elif isinstance(self.next_invoice_date, datetime.datetime):
            next_invoice_date = self.next_invoice_date.isoformat()
        else:
            next_invoice_date = self.next_invoice_date

        next_invoice_base_amount = self.next_invoice_base_amount

        coupon_id: None | str | Unset
        if isinstance(self.coupon_id, Unset):
            coupon_id = UNSET
        elif isinstance(self.coupon_id, UUID):
            coupon_id = str(self.coupon_id)
        else:
            coupon_id = self.coupon_id

        discount_active = self.discount_active

        outstanding: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.outstanding, Unset):
            outstanding = []
            for outstanding_item_data in self.outstanding:
                outstanding_item = outstanding_item_data.to_dict()
                outstanding.append(outstanding_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if subscription_id is not UNSET:
            field_dict["subscription_id"] = subscription_id
        if status is not UNSET:
            field_dict["status"] = status
        if currency is not UNSET:
            field_dict["currency"] = currency
        if mrr is not UNSET:
            field_dict["mrr"] = mrr
        if recurring_amount is not UNSET:
            field_dict["recurring_amount"] = recurring_amount
        if interval_unit is not UNSET:
            field_dict["interval_unit"] = interval_unit
        if interval_count is not UNSET:
            field_dict["interval_count"] = interval_count
        if current_period_start is not UNSET:
            field_dict["current_period_start"] = current_period_start
        if current_period_end is not UNSET:
            field_dict["current_period_end"] = current_period_end
        if next_invoice_date is not UNSET:
            field_dict["next_invoice_date"] = next_invoice_date
        if next_invoice_base_amount is not UNSET:
            field_dict["next_invoice_base_amount"] = next_invoice_base_amount
        if coupon_id is not UNSET:
            field_dict["coupon_id"] = coupon_id
        if discount_active is not UNSET:
            field_dict["discount_active"] = discount_active
        if outstanding is not UNSET:
            field_dict["outstanding"] = outstanding

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_subscription_financial_summary_response_200_data_outstanding_item import (
            GetSubscriptionFinancialSummaryResponse200DataOutstandingItem,
        )

        d = dict(src_dict)
        _subscription_id = d.pop("subscription_id", UNSET)
        subscription_id: UUID | Unset
        if isinstance(_subscription_id, Unset):
            subscription_id = UNSET
        else:
            subscription_id = UUID(_subscription_id)

        status = d.pop("status", UNSET)

        currency = d.pop("currency", UNSET)

        mrr = d.pop("mrr", UNSET)

        recurring_amount = d.pop("recurring_amount", UNSET)

        interval_unit = d.pop("interval_unit", UNSET)

        interval_count = d.pop("interval_count", UNSET)

        _current_period_start = d.pop("current_period_start", UNSET)
        current_period_start: datetime.datetime | Unset
        if isinstance(_current_period_start, Unset):
            current_period_start = UNSET
        else:
            current_period_start = datetime.datetime.fromisoformat(_current_period_start)

        _current_period_end = d.pop("current_period_end", UNSET)
        current_period_end: datetime.datetime | Unset
        if isinstance(_current_period_end, Unset):
            current_period_end = UNSET
        else:
            current_period_end = datetime.datetime.fromisoformat(_current_period_end)

        def _parse_next_invoice_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_invoice_date_type_0 = datetime.datetime.fromisoformat(data)

                return next_invoice_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        next_invoice_date = _parse_next_invoice_date(d.pop("next_invoice_date", UNSET))

        next_invoice_base_amount = d.pop("next_invoice_base_amount", UNSET)

        def _parse_coupon_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                coupon_id_type_0 = UUID(data)

                return coupon_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        coupon_id = _parse_coupon_id(d.pop("coupon_id", UNSET))

        discount_active = d.pop("discount_active", UNSET)

        _outstanding = d.pop("outstanding", UNSET)
        outstanding: list[GetSubscriptionFinancialSummaryResponse200DataOutstandingItem] | Unset = UNSET
        if _outstanding is not UNSET:
            outstanding = []
            for outstanding_item_data in _outstanding:
                outstanding_item = GetSubscriptionFinancialSummaryResponse200DataOutstandingItem.from_dict(
                    outstanding_item_data
                )

                outstanding.append(outstanding_item)

        get_subscription_financial_summary_response_200_data = cls(
            subscription_id=subscription_id,
            status=status,
            currency=currency,
            mrr=mrr,
            recurring_amount=recurring_amount,
            interval_unit=interval_unit,
            interval_count=interval_count,
            current_period_start=current_period_start,
            current_period_end=current_period_end,
            next_invoice_date=next_invoice_date,
            next_invoice_base_amount=next_invoice_base_amount,
            coupon_id=coupon_id,
            discount_active=discount_active,
            outstanding=outstanding,
        )

        get_subscription_financial_summary_response_200_data.additional_properties = d
        return get_subscription_financial_summary_response_200_data

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
