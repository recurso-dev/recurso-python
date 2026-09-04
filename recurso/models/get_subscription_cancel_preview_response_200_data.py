from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetSubscriptionCancelPreviewResponse200Data")


@_attrs_define
class GetSubscriptionCancelPreviewResponse200Data:
    """
    Attributes:
        subscription_id (UUID | Unset):
        immediately (bool | Unset):
        effective_date (datetime.datetime | Unset):
        resulting_status (str | Unset):
        cancel_at_period_end (bool | Unset):
        currency (str | Unset):
        deferred_revenue_forfeited (int | Unset):
        recognized_as_breakage (int | Unset):
        avoided_future_recurring (int | Unset):
        flat_fee_refund (int | Unset): Always 0 — flat fee paid in advance
    """

    subscription_id: UUID | Unset = UNSET
    immediately: bool | Unset = UNSET
    effective_date: datetime.datetime | Unset = UNSET
    resulting_status: str | Unset = UNSET
    cancel_at_period_end: bool | Unset = UNSET
    currency: str | Unset = UNSET
    deferred_revenue_forfeited: int | Unset = UNSET
    recognized_as_breakage: int | Unset = UNSET
    avoided_future_recurring: int | Unset = UNSET
    flat_fee_refund: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        subscription_id: str | Unset = UNSET
        if not isinstance(self.subscription_id, Unset):
            subscription_id = str(self.subscription_id)

        immediately = self.immediately

        effective_date: str | Unset = UNSET
        if not isinstance(self.effective_date, Unset):
            effective_date = self.effective_date.isoformat()

        resulting_status = self.resulting_status

        cancel_at_period_end = self.cancel_at_period_end

        currency = self.currency

        deferred_revenue_forfeited = self.deferred_revenue_forfeited

        recognized_as_breakage = self.recognized_as_breakage

        avoided_future_recurring = self.avoided_future_recurring

        flat_fee_refund = self.flat_fee_refund

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if subscription_id is not UNSET:
            field_dict["subscription_id"] = subscription_id
        if immediately is not UNSET:
            field_dict["immediately"] = immediately
        if effective_date is not UNSET:
            field_dict["effective_date"] = effective_date
        if resulting_status is not UNSET:
            field_dict["resulting_status"] = resulting_status
        if cancel_at_period_end is not UNSET:
            field_dict["cancel_at_period_end"] = cancel_at_period_end
        if currency is not UNSET:
            field_dict["currency"] = currency
        if deferred_revenue_forfeited is not UNSET:
            field_dict["deferred_revenue_forfeited"] = deferred_revenue_forfeited
        if recognized_as_breakage is not UNSET:
            field_dict["recognized_as_breakage"] = recognized_as_breakage
        if avoided_future_recurring is not UNSET:
            field_dict["avoided_future_recurring"] = avoided_future_recurring
        if flat_fee_refund is not UNSET:
            field_dict["flat_fee_refund"] = flat_fee_refund

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _subscription_id = d.pop("subscription_id", UNSET)
        subscription_id: UUID | Unset
        if isinstance(_subscription_id, Unset):
            subscription_id = UNSET
        else:
            subscription_id = UUID(_subscription_id)

        immediately = d.pop("immediately", UNSET)

        _effective_date = d.pop("effective_date", UNSET)
        effective_date: datetime.datetime | Unset
        if isinstance(_effective_date, Unset):
            effective_date = UNSET
        else:
            effective_date = datetime.datetime.fromisoformat(_effective_date)

        resulting_status = d.pop("resulting_status", UNSET)

        cancel_at_period_end = d.pop("cancel_at_period_end", UNSET)

        currency = d.pop("currency", UNSET)

        deferred_revenue_forfeited = d.pop("deferred_revenue_forfeited", UNSET)

        recognized_as_breakage = d.pop("recognized_as_breakage", UNSET)

        avoided_future_recurring = d.pop("avoided_future_recurring", UNSET)

        flat_fee_refund = d.pop("flat_fee_refund", UNSET)

        get_subscription_cancel_preview_response_200_data = cls(
            subscription_id=subscription_id,
            immediately=immediately,
            effective_date=effective_date,
            resulting_status=resulting_status,
            cancel_at_period_end=cancel_at_period_end,
            currency=currency,
            deferred_revenue_forfeited=deferred_revenue_forfeited,
            recognized_as_breakage=recognized_as_breakage,
            avoided_future_recurring=avoided_future_recurring,
            flat_fee_refund=flat_fee_refund,
        )

        get_subscription_cancel_preview_response_200_data.additional_properties = d
        return get_subscription_cancel_preview_response_200_data

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
