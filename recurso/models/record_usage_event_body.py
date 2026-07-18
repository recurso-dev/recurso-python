from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.record_usage_event_body_properties import RecordUsageEventBodyProperties


T = TypeVar("T", bound="RecordUsageEventBody")


@_attrs_define
class RecordUsageEventBody:
    """
    Attributes:
        subscription_id (UUID):
        customer_id (UUID):
        dimension (str):
        quantity (int):
        properties (RecordUsageEventBodyProperties | Unset): Optional free-form attributes (max 20; keys ≤100 chars,
            values ≤255). The `unique` billable-metric aggregation counts distinct values of one property.
    """

    subscription_id: UUID
    customer_id: UUID
    dimension: str
    quantity: int
    properties: RecordUsageEventBodyProperties | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        subscription_id = str(self.subscription_id)

        customer_id = str(self.customer_id)

        dimension = self.dimension

        quantity = self.quantity

        properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.record_usage_event_body_properties import RecordUsageEventBodyProperties

        d = dict(src_dict)
        subscription_id = UUID(d.pop("subscription_id"))

        customer_id = UUID(d.pop("customer_id"))

        dimension = d.pop("dimension")

        quantity = d.pop("quantity")

        _properties = d.pop("properties", UNSET)
        properties: RecordUsageEventBodyProperties | Unset
        if isinstance(_properties, Unset):
            properties = UNSET
        else:
            properties = RecordUsageEventBodyProperties.from_dict(_properties)

        record_usage_event_body = cls(
            subscription_id=subscription_id,
            customer_id=customer_id,
            dimension=dimension,
            quantity=quantity,
            properties=properties,
        )

        record_usage_event_body.additional_properties = d
        return record_usage_event_body

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
