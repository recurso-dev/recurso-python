from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.billable_metric_input_aggregation_type import BillableMetricInputAggregationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BillableMetricInput")


@_attrs_define
class BillableMetricInput:
    """
    Attributes:
        name (str):
        code (str): Doubles as the usage event dimension; immutable after create.
        aggregation_type (BillableMetricInputAggregationType):
        field_name (str | Unset): Required for `unique` (property) and `percentile` (1-99); forbidden otherwise.
        expression (str | Unset): Required for `custom` (a per-event formula over `quantity`/`properties.*`, summed
            over the period); forbidden otherwise.
    """

    name: str
    code: str
    aggregation_type: BillableMetricInputAggregationType
    field_name: str | Unset = UNSET
    expression: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        code = self.code

        aggregation_type = self.aggregation_type.value

        field_name = self.field_name

        expression = self.expression

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "code": code,
                "aggregation_type": aggregation_type,
            }
        )
        if field_name is not UNSET:
            field_dict["field_name"] = field_name
        if expression is not UNSET:
            field_dict["expression"] = expression

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        code = d.pop("code")

        aggregation_type = BillableMetricInputAggregationType(d.pop("aggregation_type"))

        field_name = d.pop("field_name", UNSET)

        expression = d.pop("expression", UNSET)

        billable_metric_input = cls(
            name=name,
            code=code,
            aggregation_type=aggregation_type,
            field_name=field_name,
            expression=expression,
        )

        billable_metric_input.additional_properties = d
        return billable_metric_input

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
