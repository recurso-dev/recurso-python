from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_billing_status_response_200_billing_status import GetBillingStatusResponse200BillingStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetBillingStatusResponse200")


@_attrs_define
class GetBillingStatusResponse200:
    """
    Attributes:
        billing_status (GetBillingStatusResponse200BillingStatus | Unset):
        plan_tier (str | Unset):
        trial_ends_at (datetime.datetime | Unset):
        trial_days_left (int | Unset):
        trial_expired (bool | Unset):
    """

    billing_status: GetBillingStatusResponse200BillingStatus | Unset = UNSET
    plan_tier: str | Unset = UNSET
    trial_ends_at: datetime.datetime | Unset = UNSET
    trial_days_left: int | Unset = UNSET
    trial_expired: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        billing_status: str | Unset = UNSET
        if not isinstance(self.billing_status, Unset):
            billing_status = self.billing_status.value

        plan_tier = self.plan_tier

        trial_ends_at: str | Unset = UNSET
        if not isinstance(self.trial_ends_at, Unset):
            trial_ends_at = self.trial_ends_at.isoformat()

        trial_days_left = self.trial_days_left

        trial_expired = self.trial_expired

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if billing_status is not UNSET:
            field_dict["billing_status"] = billing_status
        if plan_tier is not UNSET:
            field_dict["plan_tier"] = plan_tier
        if trial_ends_at is not UNSET:
            field_dict["trial_ends_at"] = trial_ends_at
        if trial_days_left is not UNSET:
            field_dict["trial_days_left"] = trial_days_left
        if trial_expired is not UNSET:
            field_dict["trial_expired"] = trial_expired

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _billing_status = d.pop("billing_status", UNSET)
        billing_status: GetBillingStatusResponse200BillingStatus | Unset
        if isinstance(_billing_status, Unset):
            billing_status = UNSET
        else:
            billing_status = GetBillingStatusResponse200BillingStatus(_billing_status)

        plan_tier = d.pop("plan_tier", UNSET)

        _trial_ends_at = d.pop("trial_ends_at", UNSET)
        trial_ends_at: datetime.datetime | Unset
        if isinstance(_trial_ends_at, Unset):
            trial_ends_at = UNSET
        else:
            trial_ends_at = datetime.datetime.fromisoformat(_trial_ends_at)

        trial_days_left = d.pop("trial_days_left", UNSET)

        trial_expired = d.pop("trial_expired", UNSET)

        get_billing_status_response_200 = cls(
            billing_status=billing_status,
            plan_tier=plan_tier,
            trial_ends_at=trial_ends_at,
            trial_days_left=trial_days_left,
            trial_expired=trial_expired,
        )

        get_billing_status_response_200.additional_properties = d
        return get_billing_status_response_200

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
