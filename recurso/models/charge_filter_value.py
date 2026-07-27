from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.charge_filter_value_amounts import ChargeFilterValueAmounts


T = TypeVar("T", bound="ChargeFilterValue")


@_attrs_define
class ChargeFilterValue:
    """
    Attributes:
        value (str): The property value this band prices.
        amounts (ChargeFilterValueAmounts):
    """

    value: str
    amounts: ChargeFilterValueAmounts
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        amounts = self.amounts.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "value": value,
                "amounts": amounts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.charge_filter_value_amounts import ChargeFilterValueAmounts

        d = dict(src_dict)
        value = d.pop("value")

        amounts = ChargeFilterValueAmounts.from_dict(d.pop("amounts"))

        charge_filter_value = cls(
            value=value,
            amounts=amounts,
        )

        charge_filter_value.additional_properties = d
        return charge_filter_value

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
