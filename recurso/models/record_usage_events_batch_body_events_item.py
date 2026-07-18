from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.record_usage_events_batch_body_events_item_properties import (
        RecordUsageEventsBatchBodyEventsItemProperties,
    )


T = TypeVar("T", bound="RecordUsageEventsBatchBodyEventsItem")


@_attrs_define
class RecordUsageEventsBatchBodyEventsItem:
    """
    Attributes:
        subscription_id (UUID):
        customer_id (UUID):
        dimension (str):
        quantity (int):
        properties (RecordUsageEventsBatchBodyEventsItemProperties | Unset):
        transaction_id (str | Unset):
    """

    subscription_id: UUID
    customer_id: UUID
    dimension: str
    quantity: int
    properties: RecordUsageEventsBatchBodyEventsItemProperties | Unset = UNSET
    transaction_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        subscription_id = str(self.subscription_id)

        customer_id = str(self.customer_id)

        dimension = self.dimension

        quantity = self.quantity

        properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        transaction_id = self.transaction_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "subscription_id": subscription_id,
                "customer_id": customer_id,
                "dimension": dimension,
                "quantity": quantity,
            }
        )
        if properties is not UNSET:
            field_dict["properties"] = properties
        if transaction_id is not UNSET:
            field_dict["transaction_id"] = transaction_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.record_usage_events_batch_body_events_item_properties import (
            RecordUsageEventsBatchBodyEventsItemProperties,
        )

        d = dict(src_dict)
        subscription_id = UUID(d.pop("subscription_id"))

        customer_id = UUID(d.pop("customer_id"))

        dimension = d.pop("dimension")

        quantity = d.pop("quantity")

        _properties = d.pop("properties", UNSET)
        properties: RecordUsageEventsBatchBodyEventsItemProperties | Unset
        if isinstance(_properties, Unset):
            properties = UNSET
        else:
            properties = RecordUsageEventsBatchBodyEventsItemProperties.from_dict(_properties)

        transaction_id = d.pop("transaction_id", UNSET)

        record_usage_events_batch_body_events_item = cls(
            subscription_id=subscription_id,
            customer_id=customer_id,
            dimension=dimension,
            quantity=quantity,
            properties=properties,
            transaction_id=transaction_id,
        )

        record_usage_events_batch_body_events_item.additional_properties = d
        return record_usage_events_batch_body_events_item

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
