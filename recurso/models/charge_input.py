from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.charge_input_charge_model import ChargeInputChargeModel
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.charge_input_amounts import ChargeInputAmounts


T = TypeVar("T", bound="ChargeInput")


@_attrs_define
class ChargeInput:
    """
    Attributes:
        metric_id (UUID):
        charge_model (ChargeInputChargeModel):
        amounts (ChargeInputAmounts):
        pay_in_advance (bool | Unset): Non-cumulative models only (per_unit/percentage/dynamic).
        hsn_code (str | Unset):
    """

    metric_id: UUID
    charge_model: ChargeInputChargeModel
    amounts: ChargeInputAmounts
    pay_in_advance: bool | Unset = UNSET
    hsn_code: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        metric_id = str(self.metric_id)

        charge_model = self.charge_model.value

        amounts = self.amounts.to_dict()

        pay_in_advance = self.pay_in_advance

        hsn_code = self.hsn_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "metric_id": metric_id,
                "charge_model": charge_model,
                "amounts": amounts,
            }
        )
        if pay_in_advance is not UNSET:
            field_dict["pay_in_advance"] = pay_in_advance
        if hsn_code is not UNSET:
            field_dict["hsn_code"] = hsn_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.charge_input_amounts import ChargeInputAmounts

        d = dict(src_dict)
        metric_id = UUID(d.pop("metric_id"))

        charge_model = ChargeInputChargeModel(d.pop("charge_model"))

        amounts = ChargeInputAmounts.from_dict(d.pop("amounts"))

        pay_in_advance = d.pop("pay_in_advance", UNSET)

        hsn_code = d.pop("hsn_code", UNSET)

        charge_input = cls(
            metric_id=metric_id,
            charge_model=charge_model,
            amounts=amounts,
            pay_in_advance=pay_in_advance,
            hsn_code=hsn_code,
        )

        charge_input.additional_properties = d
        return charge_input

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
