from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.compare_chargebee_import_body_customers_item import CompareChargebeeImportBodyCustomersItem
    from ..models.compare_chargebee_import_body_plans_item import CompareChargebeeImportBodyPlansItem
    from ..models.compare_chargebee_import_body_subscriptions_item import CompareChargebeeImportBodySubscriptionsItem


T = TypeVar("T", bound="CompareChargebeeImportBody")


@_attrs_define
class CompareChargebeeImportBody:
    """
    Attributes:
        customers (list[CompareChargebeeImportBodyCustomersItem] | Unset):
        plans (list[CompareChargebeeImportBodyPlansItem] | Unset):
        subscriptions (list[CompareChargebeeImportBodySubscriptionsItem] | Unset):
    """

    customers: list[CompareChargebeeImportBodyCustomersItem] | Unset = UNSET
    plans: list[CompareChargebeeImportBodyPlansItem] | Unset = UNSET
    subscriptions: list[CompareChargebeeImportBodySubscriptionsItem] | Unset = UNSET
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
        from ..models.compare_chargebee_import_body_customers_item import CompareChargebeeImportBodyCustomersItem
        from ..models.compare_chargebee_import_body_plans_item import CompareChargebeeImportBodyPlansItem
        from ..models.compare_chargebee_import_body_subscriptions_item import (
            CompareChargebeeImportBodySubscriptionsItem,
        )

        d = dict(src_dict)
        _customers = d.pop("customers", UNSET)
        customers: list[CompareChargebeeImportBodyCustomersItem] | Unset = UNSET
        if _customers is not UNSET:
            customers = []
            for customers_item_data in _customers:
                customers_item = CompareChargebeeImportBodyCustomersItem.from_dict(customers_item_data)

                customers.append(customers_item)

        _plans = d.pop("plans", UNSET)
        plans: list[CompareChargebeeImportBodyPlansItem] | Unset = UNSET
        if _plans is not UNSET:
            plans = []
            for plans_item_data in _plans:
                plans_item = CompareChargebeeImportBodyPlansItem.from_dict(plans_item_data)

                plans.append(plans_item)

        _subscriptions = d.pop("subscriptions", UNSET)
        subscriptions: list[CompareChargebeeImportBodySubscriptionsItem] | Unset = UNSET
        if _subscriptions is not UNSET:
            subscriptions = []
            for subscriptions_item_data in _subscriptions:
                subscriptions_item = CompareChargebeeImportBodySubscriptionsItem.from_dict(subscriptions_item_data)

                subscriptions.append(subscriptions_item)

        compare_chargebee_import_body = cls(
            customers=customers,
            plans=plans,
            subscriptions=subscriptions,
        )

        compare_chargebee_import_body.additional_properties = d
        return compare_chargebee_import_body

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
