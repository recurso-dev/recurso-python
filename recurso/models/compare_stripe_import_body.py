from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.compare_stripe_import_body_customers_item import CompareStripeImportBodyCustomersItem
    from ..models.compare_stripe_import_body_payment_methods_item import CompareStripeImportBodyPaymentMethodsItem
    from ..models.compare_stripe_import_body_prices_item import CompareStripeImportBodyPricesItem
    from ..models.compare_stripe_import_body_products_item import CompareStripeImportBodyProductsItem
    from ..models.compare_stripe_import_body_subscriptions_item import CompareStripeImportBodySubscriptionsItem


T = TypeVar("T", bound="CompareStripeImportBody")


@_attrs_define
class CompareStripeImportBody:
    """
    Attributes:
        customers (list[CompareStripeImportBodyCustomersItem] | Unset):
        products (list[CompareStripeImportBodyProductsItem] | Unset):
        prices (list[CompareStripeImportBodyPricesItem] | Unset):
        subscriptions (list[CompareStripeImportBodySubscriptionsItem] | Unset):
        payment_methods (list[CompareStripeImportBodyPaymentMethodsItem] | Unset):
    """

    customers: list[CompareStripeImportBodyCustomersItem] | Unset = UNSET
    products: list[CompareStripeImportBodyProductsItem] | Unset = UNSET
    prices: list[CompareStripeImportBodyPricesItem] | Unset = UNSET
    subscriptions: list[CompareStripeImportBodySubscriptionsItem] | Unset = UNSET
    payment_methods: list[CompareStripeImportBodyPaymentMethodsItem] | Unset = UNSET
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
        from ..models.compare_stripe_import_body_customers_item import CompareStripeImportBodyCustomersItem
        from ..models.compare_stripe_import_body_payment_methods_item import CompareStripeImportBodyPaymentMethodsItem
        from ..models.compare_stripe_import_body_prices_item import CompareStripeImportBodyPricesItem
        from ..models.compare_stripe_import_body_products_item import CompareStripeImportBodyProductsItem
        from ..models.compare_stripe_import_body_subscriptions_item import CompareStripeImportBodySubscriptionsItem

        d = dict(src_dict)
        _customers = d.pop("customers", UNSET)
        customers: list[CompareStripeImportBodyCustomersItem] | Unset = UNSET
        if _customers is not UNSET:
            customers = []
            for customers_item_data in _customers:
                customers_item = CompareStripeImportBodyCustomersItem.from_dict(customers_item_data)

                customers.append(customers_item)

        _products = d.pop("products", UNSET)
        products: list[CompareStripeImportBodyProductsItem] | Unset = UNSET
        if _products is not UNSET:
            products = []
            for products_item_data in _products:
                products_item = CompareStripeImportBodyProductsItem.from_dict(products_item_data)

                products.append(products_item)

        _prices = d.pop("prices", UNSET)
        prices: list[CompareStripeImportBodyPricesItem] | Unset = UNSET
        if _prices is not UNSET:
            prices = []
            for prices_item_data in _prices:
                prices_item = CompareStripeImportBodyPricesItem.from_dict(prices_item_data)

                prices.append(prices_item)

        _subscriptions = d.pop("subscriptions", UNSET)
        subscriptions: list[CompareStripeImportBodySubscriptionsItem] | Unset = UNSET
        if _subscriptions is not UNSET:
            subscriptions = []
            for subscriptions_item_data in _subscriptions:
                subscriptions_item = CompareStripeImportBodySubscriptionsItem.from_dict(subscriptions_item_data)

                subscriptions.append(subscriptions_item)

        _payment_methods = d.pop("payment_methods", UNSET)
        payment_methods: list[CompareStripeImportBodyPaymentMethodsItem] | Unset = UNSET
        if _payment_methods is not UNSET:
            payment_methods = []
            for payment_methods_item_data in _payment_methods:
                payment_methods_item = CompareStripeImportBodyPaymentMethodsItem.from_dict(payment_methods_item_data)

                payment_methods.append(payment_methods_item)

        compare_stripe_import_body = cls(
            customers=customers,
            products=products,
            prices=prices,
            subscriptions=subscriptions,
            payment_methods=payment_methods,
        )

        compare_stripe_import_body.additional_properties = d
        return compare_stripe_import_body

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
