from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.preview_revenue_cat_import_body_products_item import PreviewRevenueCatImportBodyProductsItem
    from ..models.preview_revenue_cat_import_body_subscribers_item import PreviewRevenueCatImportBodySubscribersItem


T = TypeVar("T", bound="PreviewRevenueCatImportBody")


@_attrs_define
class PreviewRevenueCatImportBody:
    """
    Attributes:
        subscribers (list[PreviewRevenueCatImportBodySubscribersItem] | Unset):
        products (list[PreviewRevenueCatImportBodyProductsItem] | Unset):
    """

    subscribers: list[PreviewRevenueCatImportBodySubscribersItem] | Unset = UNSET
    products: list[PreviewRevenueCatImportBodyProductsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        subscribers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.subscribers, Unset):
            subscribers = []
            for subscribers_item_data in self.subscribers:
                subscribers_item = subscribers_item_data.to_dict()
                subscribers.append(subscribers_item)

        products: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.products, Unset):
            products = []
            for products_item_data in self.products:
                products_item = products_item_data.to_dict()
                products.append(products_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if subscribers is not UNSET:
            field_dict["subscribers"] = subscribers
        if products is not UNSET:
            field_dict["products"] = products

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.preview_revenue_cat_import_body_products_item import PreviewRevenueCatImportBodyProductsItem
        from ..models.preview_revenue_cat_import_body_subscribers_item import PreviewRevenueCatImportBodySubscribersItem

        d = dict(src_dict)
        _subscribers = d.pop("subscribers", UNSET)
        subscribers: list[PreviewRevenueCatImportBodySubscribersItem] | Unset = UNSET
        if _subscribers is not UNSET:
            subscribers = []
            for subscribers_item_data in _subscribers:
                subscribers_item = PreviewRevenueCatImportBodySubscribersItem.from_dict(subscribers_item_data)

                subscribers.append(subscribers_item)

        _products = d.pop("products", UNSET)
        products: list[PreviewRevenueCatImportBodyProductsItem] | Unset = UNSET
        if _products is not UNSET:
            products = []
            for products_item_data in _products:
                products_item = PreviewRevenueCatImportBodyProductsItem.from_dict(products_item_data)

                products.append(products_item)

        preview_revenue_cat_import_body = cls(
            subscribers=subscribers,
            products=products,
        )

        preview_revenue_cat_import_body.additional_properties = d
        return preview_revenue_cat_import_body

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
