from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.commit_chargebee_import_body_customers_item import CommitChargebeeImportBodyCustomersItem
    from ..models.commit_chargebee_import_body_plans_item import CommitChargebeeImportBodyPlansItem
    from ..models.commit_chargebee_import_body_subscriptions_item import CommitChargebeeImportBodySubscriptionsItem


T = TypeVar("T", bound="CommitChargebeeImportBody")


@_attrs_define
class CommitChargebeeImportBody:
    """
    Attributes:
        customers (list[CommitChargebeeImportBodyCustomersItem] | Unset):
        plans (list[CommitChargebeeImportBodyPlansItem] | Unset):
        subscriptions (list[CommitChargebeeImportBodySubscriptionsItem] | Unset):
    """

    customers: list[CommitChargebeeImportBodyCustomersItem] | Unset = UNSET
    plans: list[CommitChargebeeImportBodyPlansItem] | Unset = UNSET
    subscriptions: list[CommitChargebeeImportBodySubscriptionsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        customers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.customers, Unset):
            customers = []
            for customers_item_data in self.customers:
                customers_item = customers_item_data.to_dict()
                customers.append(customers_item)

        plans: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.plans, Unset):
            plans = []
            for plans_item_data in self.plans:
                plans_item = plans_item_data.to_dict()
                plans.append(plans_item)

        subscriptions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.subscriptions, Unset):
            subscriptions = []
            for subscriptions_item_data in self.subscriptions:
                subscriptions_item = subscriptions_item_data.to_dict()
                subscriptions.append(subscriptions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if customers is not UNSET:
            field_dict["customers"] = customers
        if plans is not UNSET:
            field_dict["plans"] = plans
        if subscriptions is not UNSET:
            field_dict["subscriptions"] = subscriptions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.commit_chargebee_import_body_customers_item import CommitChargebeeImportBodyCustomersItem
        from ..models.commit_chargebee_import_body_plans_item import CommitChargebeeImportBodyPlansItem
        from ..models.commit_chargebee_import_body_subscriptions_item import CommitChargebeeImportBodySubscriptionsItem

        d = dict(src_dict)
        _customers = d.pop("customers", UNSET)
        customers: list[CommitChargebeeImportBodyCustomersItem] | Unset = UNSET
        if _customers is not UNSET:
            customers = []
            for customers_item_data in _customers:
                customers_item = CommitChargebeeImportBodyCustomersItem.from_dict(customers_item_data)

                customers.append(customers_item)

        _plans = d.pop("plans", UNSET)
        plans: list[CommitChargebeeImportBodyPlansItem] | Unset = UNSET
        if _plans is not UNSET:
            plans = []
            for plans_item_data in _plans:
                plans_item = CommitChargebeeImportBodyPlansItem.from_dict(plans_item_data)

                plans.append(plans_item)

        _subscriptions = d.pop("subscriptions", UNSET)
        subscriptions: list[CommitChargebeeImportBodySubscriptionsItem] | Unset = UNSET
        if _subscriptions is not UNSET:
            subscriptions = []
            for subscriptions_item_data in _subscriptions:
                subscriptions_item = CommitChargebeeImportBodySubscriptionsItem.from_dict(subscriptions_item_data)

                subscriptions.append(subscriptions_item)

        commit_chargebee_import_body = cls(
            customers=customers,
            plans=plans,
            subscriptions=subscriptions,
        )

        commit_chargebee_import_body.additional_properties = d
        return commit_chargebee_import_body

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
