from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.commit_stripe_import_body_customers_item import CommitStripeImportBodyCustomersItem
    from ..models.commit_stripe_import_body_payment_methods_item import CommitStripeImportBodyPaymentMethodsItem
    from ..models.commit_stripe_import_body_prices_item import CommitStripeImportBodyPricesItem
    from ..models.commit_stripe_import_body_products_item import CommitStripeImportBodyProductsItem
    from ..models.commit_stripe_import_body_subscriptions_item import CommitStripeImportBodySubscriptionsItem


T = TypeVar("T", bound="CommitStripeImportBody")


@_attrs_define
class CommitStripeImportBody:
    """
    Attributes:
        customers (list[CommitStripeImportBodyCustomersItem] | Unset):
        products (list[CommitStripeImportBodyProductsItem] | Unset):
        prices (list[CommitStripeImportBodyPricesItem] | Unset):
        subscriptions (list[CommitStripeImportBodySubscriptionsItem] | Unset):
        payment_methods (list[CommitStripeImportBodyPaymentMethodsItem] | Unset):
    """

    customers: list[CommitStripeImportBodyCustomersItem] | Unset = UNSET
    products: list[CommitStripeImportBodyProductsItem] | Unset = UNSET
    prices: list[CommitStripeImportBodyPricesItem] | Unset = UNSET
    subscriptions: list[CommitStripeImportBodySubscriptionsItem] | Unset = UNSET
    payment_methods: list[CommitStripeImportBodyPaymentMethodsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        customers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.customers, Unset):
            customers = []
            for customers_item_data in self.customers:
                customers_item = customers_item_data.to_dict()
                customers.append(customers_item)

        products: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.products, Unset):
            products = []
            for products_item_data in self.products:
                products_item = products_item_data.to_dict()
                products.append(products_item)

        prices: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.prices, Unset):
            prices = []
            for prices_item_data in self.prices:
                prices_item = prices_item_data.to_dict()
                prices.append(prices_item)

        subscriptions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.subscriptions, Unset):
            subscriptions = []
            for subscriptions_item_data in self.subscriptions:
                subscriptions_item = subscriptions_item_data.to_dict()
                subscriptions.append(subscriptions_item)

        payment_methods: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.payment_methods, Unset):
            payment_methods = []
            for payment_methods_item_data in self.payment_methods:
                payment_methods_item = payment_methods_item_data.to_dict()
                payment_methods.append(payment_methods_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if customers is not UNSET:
            field_dict["customers"] = customers
        if products is not UNSET:
            field_dict["products"] = products
        if prices is not UNSET:
            field_dict["prices"] = prices
        if subscriptions is not UNSET:
            field_dict["subscriptions"] = subscriptions
        if payment_methods is not UNSET:
            field_dict["payment_methods"] = payment_methods

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.commit_stripe_import_body_customers_item import CommitStripeImportBodyCustomersItem
        from ..models.commit_stripe_import_body_payment_methods_item import CommitStripeImportBodyPaymentMethodsItem
        from ..models.commit_stripe_import_body_prices_item import CommitStripeImportBodyPricesItem
        from ..models.commit_stripe_import_body_products_item import CommitStripeImportBodyProductsItem
        from ..models.commit_stripe_import_body_subscriptions_item import CommitStripeImportBodySubscriptionsItem

        d = dict(src_dict)
        _customers = d.pop("customers", UNSET)
        customers: list[CommitStripeImportBodyCustomersItem] | Unset = UNSET
        if _customers is not UNSET:
            customers = []
            for customers_item_data in _customers:
                customers_item = CommitStripeImportBodyCustomersItem.from_dict(customers_item_data)

                customers.append(customers_item)

        _products = d.pop("products", UNSET)
        products: list[CommitStripeImportBodyProductsItem] | Unset = UNSET
        if _products is not UNSET:
            products = []
            for products_item_data in _products:
                products_item = CommitStripeImportBodyProductsItem.from_dict(products_item_data)

                products.append(products_item)

        _prices = d.pop("prices", UNSET)
        prices: list[CommitStripeImportBodyPricesItem] | Unset = UNSET
        if _prices is not UNSET:
            prices = []
            for prices_item_data in _prices:
                prices_item = CommitStripeImportBodyPricesItem.from_dict(prices_item_data)

                prices.append(prices_item)

        _subscriptions = d.pop("subscriptions", UNSET)
        subscriptions: list[CommitStripeImportBodySubscriptionsItem] | Unset = UNSET
        if _subscriptions is not UNSET:
            subscriptions = []
            for subscriptions_item_data in _subscriptions:
                subscriptions_item = CommitStripeImportBodySubscriptionsItem.from_dict(subscriptions_item_data)

                subscriptions.append(subscriptions_item)

        _payment_methods = d.pop("payment_methods", UNSET)
        payment_methods: list[CommitStripeImportBodyPaymentMethodsItem] | Unset = UNSET
        if _payment_methods is not UNSET:
            payment_methods = []
            for payment_methods_item_data in _payment_methods:
                payment_methods_item = CommitStripeImportBodyPaymentMethodsItem.from_dict(payment_methods_item_data)

                payment_methods.append(payment_methods_item)

        commit_stripe_import_body = cls(
            customers=customers,
            products=products,
            prices=prices,
            subscriptions=subscriptions,
            payment_methods=payment_methods,
        )

        commit_stripe_import_body.additional_properties = d
        return commit_stripe_import_body

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
