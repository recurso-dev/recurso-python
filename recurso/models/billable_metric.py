from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.billable_metric_aggregation_type import BillableMetricAggregationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BillableMetric")


@_attrs_define
class BillableMetric:
    """A tenant-defined meter over usage events; `code` equals the event `dimension` it aggregates and is unique per
    tenant.

        Attributes:
            id (UUID | Unset):
            tenant_id (UUID | Unset):
            name (str | Unset):
            code (str | Unset):
            aggregation_type (BillableMetricAggregationType | Unset):
            field_name (str | Unset): Event property counted by the `unique` aggregation.
            created_at (datetime.datetime | Unset):
            updated_at (datetime.datetime | Unset):
    """

    id: UUID | Unset = UNSET
    tenant_id: UUID | Unset = UNSET
    name: str | Unset = UNSET
    code: str | Unset = UNSET
    aggregation_type: BillableMetricAggregationType | Unset = UNSET
    field_name: str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        tenant_id: str | Unset = UNSET
        if not isinstance(self.tenant_id, Unset):
            tenant_id = str(self.tenant_id)

        name = self.name

        code = self.code

        aggregation_type: str | Unset = UNSET
        if not isinstance(self.aggregation_type, Unset):
            aggregation_type = self.aggregation_type.value

        field_name = self.field_name

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
        if tenant_id is not UNSET:
            field_dict["tenant_id"] = tenant_id
        if name is not UNSET:
            field_dict["name"] = name
        if code is not UNSET:
            field_dict["code"] = code
        if aggregation_type is not UNSET:
            field_dict["aggregation_type"] = aggregation_type
        if field_name is not UNSET:
            field_dict["field_name"] = field_name
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

        _tenant_id = d.pop("tenant_id", UNSET)
        tenant_id: UUID | Unset
        if isinstance(_tenant_id, Unset):
            tenant_id = UNSET
        else:
            tenant_id = UUID(_tenant_id)

        name = d.pop("name", UNSET)

        code = d.pop("code", UNSET)

        _aggregation_type = d.pop("aggregation_type", UNSET)
        aggregation_type: BillableMetricAggregationType | Unset
        if isinstance(_aggregation_type, Unset):
            aggregation_type = UNSET
        else:
            aggregation_type = BillableMetricAggregationType(_aggregation_type)

        field_name = d.pop("field_name", UNSET)

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

        billable_metric = cls(
            id=id,
            tenant_id=tenant_id,
            name=name,
            code=code,
            aggregation_type=aggregation_type,
            field_name=field_name,
            created_at=created_at,
            updated_at=updated_at,
        )

        billable_metric.additional_properties = d
        return billable_metric

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
