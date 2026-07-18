from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.usage_alert_threshold_type import UsageAlertThresholdType
from ..types import UNSET, Unset

T = TypeVar("T", bound="UsageAlert")


@_attrs_define
class UsageAlert:
    """A usage threshold that fires once per billing period.

    Attributes:
        id (UUID | Unset):
        subscription_id (UUID | Unset):
        metric_code (str | Unset):
        threshold_type (UsageAlertThresholdType | Unset):
        threshold (int | Unset):
        last_fired_period_start (datetime.datetime | None | Unset):
        created_at (datetime.datetime | Unset):
        updated_at (datetime.datetime | Unset):
    """

    id: UUID | Unset = UNSET
    subscription_id: UUID | Unset = UNSET
    metric_code: str | Unset = UNSET
    threshold_type: UsageAlertThresholdType | Unset = UNSET
    threshold: int | Unset = UNSET
    last_fired_period_start: datetime.datetime | None | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        subscription_id: str | Unset = UNSET
        if not isinstance(self.subscription_id, Unset):
            subscription_id = str(self.subscription_id)

        metric_code = self.metric_code

        threshold_type: str | Unset = UNSET
        if not isinstance(self.threshold_type, Unset):
            threshold_type = self.threshold_type.value

        threshold = self.threshold

        last_fired_period_start: None | str | Unset
        if isinstance(self.last_fired_period_start, Unset):
            last_fired_period_start = UNSET
        elif isinstance(self.last_fired_period_start, datetime.datetime):
            last_fired_period_start = self.last_fired_period_start.isoformat()
        else:
            last_fired_period_start = self.last_fired_period_start

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if subscription_id is not UNSET:
            field_dict["subscription_id"] = subscription_id
        if metric_code is not UNSET:
            field_dict["metric_code"] = metric_code
        if threshold_type is not UNSET:
            field_dict["threshold_type"] = threshold_type
        if threshold is not UNSET:
            field_dict["threshold"] = threshold
        if last_fired_period_start is not UNSET:
            field_dict["last_fired_period_start"] = last_fired_period_start
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        _subscription_id = d.pop("subscription_id", UNSET)
        subscription_id: UUID | Unset
        if isinstance(_subscription_id, Unset):
            subscription_id = UNSET
        else:
            subscription_id = UUID(_subscription_id)

        metric_code = d.pop("metric_code", UNSET)

        _threshold_type = d.pop("threshold_type", UNSET)
        threshold_type: UsageAlertThresholdType | Unset
        if isinstance(_threshold_type, Unset):
            threshold_type = UNSET
        else:
            threshold_type = UsageAlertThresholdType(_threshold_type)

        threshold = d.pop("threshold", UNSET)

        def _parse_last_fired_period_start(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_fired_period_start_type_0 = datetime.datetime.fromisoformat(data)

                return last_fired_period_start_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_fired_period_start = _parse_last_fired_period_start(d.pop("last_fired_period_start", UNSET))

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = datetime.datetime.fromisoformat(_updated_at)

        usage_alert = cls(
            id=id,
            subscription_id=subscription_id,
            metric_code=metric_code,
            threshold_type=threshold_type,
            threshold=threshold,
            last_fired_period_start=last_fired_period_start,
            created_at=created_at,
            updated_at=updated_at,
        )

        usage_alert.additional_properties = d
        return usage_alert

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
