from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_usage_alert_body_threshold_type import CreateUsageAlertBodyThresholdType

T = TypeVar("T", bound="CreateUsageAlertBody")


@_attrs_define
class CreateUsageAlertBody:
    """
    Attributes:
        subscription_id (UUID):
        metric_code (str):
        threshold_type (CreateUsageAlertBodyThresholdType):
        threshold (int):
    """

    subscription_id: UUID
    metric_code: str
    threshold_type: CreateUsageAlertBodyThresholdType
    threshold: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        subscription_id = str(self.subscription_id)

        metric_code = self.metric_code

        threshold_type = self.threshold_type.value

        threshold = self.threshold

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "subscription_id": subscription_id,
                "metric_code": metric_code,
                "threshold_type": threshold_type,
                "threshold": threshold,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        subscription_id = UUID(d.pop("subscription_id"))

        metric_code = d.pop("metric_code")

        threshold_type = CreateUsageAlertBodyThresholdType(d.pop("threshold_type"))

        threshold = d.pop("threshold")

        create_usage_alert_body = cls(
            subscription_id=subscription_id,
            metric_code=metric_code,
            threshold_type=threshold_type,
            threshold=threshold,
        )

        create_usage_alert_body.additional_properties = d
        return create_usage_alert_body

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
