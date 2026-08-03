from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.commit_stripe_import_response_200_created import CommitStripeImportResponse200Created
    from ..models.commit_stripe_import_response_200_failures_item import CommitStripeImportResponse200FailuresItem
    from ..models.commit_stripe_import_response_200_plan import CommitStripeImportResponse200Plan


T = TypeVar("T", bound="CommitStripeImportResponse200")


@_attrs_define
class CommitStripeImportResponse200:
    """
    Attributes:
        plan (CommitStripeImportResponse200Plan | Unset):
        created (CommitStripeImportResponse200Created | Unset):
        failures (list[CommitStripeImportResponse200FailuresItem] | Unset):
    """

    plan: CommitStripeImportResponse200Plan | Unset = UNSET
    created: CommitStripeImportResponse200Created | Unset = UNSET
    failures: list[CommitStripeImportResponse200FailuresItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        plan: dict[str, Any] | Unset = UNSET
        if not isinstance(self.plan, Unset):
            plan = self.plan.to_dict()

        created: dict[str, Any] | Unset = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.to_dict()

        failures: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.failures, Unset):
            failures = []
            for failures_item_data in self.failures:
                failures_item = failures_item_data.to_dict()
                failures.append(failures_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if plan is not UNSET:
            field_dict["plan"] = plan
        if created is not UNSET:
            field_dict["created"] = created
        if failures is not UNSET:
            field_dict["failures"] = failures

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.commit_stripe_import_response_200_created import CommitStripeImportResponse200Created
        from ..models.commit_stripe_import_response_200_failures_item import CommitStripeImportResponse200FailuresItem
        from ..models.commit_stripe_import_response_200_plan import CommitStripeImportResponse200Plan

        d = dict(src_dict)
        _plan = d.pop("plan", UNSET)
        plan: CommitStripeImportResponse200Plan | Unset
        if isinstance(_plan, Unset):
            plan = UNSET
        else:
            plan = CommitStripeImportResponse200Plan.from_dict(_plan)

        _created = d.pop("created", UNSET)
        created: CommitStripeImportResponse200Created | Unset
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = CommitStripeImportResponse200Created.from_dict(_created)

        _failures = d.pop("failures", UNSET)
        failures: list[CommitStripeImportResponse200FailuresItem] | Unset = UNSET
        if _failures is not UNSET:
            failures = []
            for failures_item_data in _failures:
                failures_item = CommitStripeImportResponse200FailuresItem.from_dict(failures_item_data)

                failures.append(failures_item)

        commit_stripe_import_response_200 = cls(
            plan=plan,
            created=created,
            failures=failures,
        )

        commit_stripe_import_response_200.additional_properties = d
        return commit_stripe_import_response_200

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
