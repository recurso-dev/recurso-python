from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.compare_count import CompareCount
    from ..models.compare_stripe_import_response_200_issues_item import CompareStripeImportResponse200IssuesItem


T = TypeVar("T", bound="CompareStripeImportResponse200")


@_attrs_define
class CompareStripeImportResponse200:
    """
    Attributes:
        source (str | Unset):
        customers (CompareCount | Unset): Migration-compare coverage for one record kind.
        plans (CompareCount | Unset): Migration-compare coverage for one record kind.
        subscriptions (CompareCount | Unset): Migration-compare coverage for one record kind.
        issues (list[CompareStripeImportResponse200IssuesItem] | Unset):
        ready (bool | Unset):
        generated_at (datetime.datetime | Unset):
    """

    source: str | Unset = UNSET
    customers: CompareCount | Unset = UNSET
    plans: CompareCount | Unset = UNSET
    subscriptions: CompareCount | Unset = UNSET
    issues: list[CompareStripeImportResponse200IssuesItem] | Unset = UNSET
    ready: bool | Unset = UNSET
    generated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source = self.source

        customers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.customers, Unset):
            customers = self.customers.to_dict()

        plans: dict[str, Any] | Unset = UNSET
        if not isinstance(self.plans, Unset):
            plans = self.plans.to_dict()

        subscriptions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.subscriptions, Unset):
            subscriptions = self.subscriptions.to_dict()

        issues: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.issues, Unset):
            issues = []
            for issues_item_data in self.issues:
                issues_item = issues_item_data.to_dict()
                issues.append(issues_item)

        ready = self.ready

        generated_at: str | Unset = UNSET
        if not isinstance(self.generated_at, Unset):
            generated_at = self.generated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if source is not UNSET:
            field_dict["source"] = source
        if customers is not UNSET:
            field_dict["customers"] = customers
        if plans is not UNSET:
            field_dict["plans"] = plans
        if subscriptions is not UNSET:
            field_dict["subscriptions"] = subscriptions
        if issues is not UNSET:
            field_dict["issues"] = issues
        if ready is not UNSET:
            field_dict["ready"] = ready
        if generated_at is not UNSET:
            field_dict["generated_at"] = generated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.compare_count import CompareCount
        from ..models.compare_stripe_import_response_200_issues_item import CompareStripeImportResponse200IssuesItem

        d = dict(src_dict)
        source = d.pop("source", UNSET)

        _customers = d.pop("customers", UNSET)
        customers: CompareCount | Unset
        if isinstance(_customers, Unset):
            customers = UNSET
        else:
            customers = CompareCount.from_dict(_customers)

        _plans = d.pop("plans", UNSET)
        plans: CompareCount | Unset
        if isinstance(_plans, Unset):
            plans = UNSET
        else:
            plans = CompareCount.from_dict(_plans)

        _subscriptions = d.pop("subscriptions", UNSET)
        subscriptions: CompareCount | Unset
        if isinstance(_subscriptions, Unset):
            subscriptions = UNSET
        else:
            subscriptions = CompareCount.from_dict(_subscriptions)

        _issues = d.pop("issues", UNSET)
        issues: list[CompareStripeImportResponse200IssuesItem] | Unset = UNSET
        if _issues is not UNSET:
            issues = []
            for issues_item_data in _issues:
                issues_item = CompareStripeImportResponse200IssuesItem.from_dict(issues_item_data)

                issues.append(issues_item)

        ready = d.pop("ready", UNSET)

        _generated_at = d.pop("generated_at", UNSET)
        generated_at: datetime.datetime | Unset
        if isinstance(_generated_at, Unset):
            generated_at = UNSET
        else:
            generated_at = datetime.datetime.fromisoformat(_generated_at)

        compare_stripe_import_response_200 = cls(
            source=source,
            customers=customers,
            plans=plans,
            subscriptions=subscriptions,
            issues=issues,
            ready=ready,
            generated_at=generated_at,
        )

        compare_stripe_import_response_200.additional_properties = d
        return compare_stripe_import_response_200

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
