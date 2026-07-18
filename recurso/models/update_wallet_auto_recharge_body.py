from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateWalletAutoRechargeBody")


@_attrs_define
class UpdateWalletAutoRechargeBody:
    """
    Attributes:
        auto_recharge_threshold (int | None | Unset):
        auto_recharge_amount (int | None | Unset):
    """

    auto_recharge_threshold: int | None | Unset = UNSET
    auto_recharge_amount: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auto_recharge_threshold: int | None | Unset
        if isinstance(self.auto_recharge_threshold, Unset):
            auto_recharge_threshold = UNSET
        else:
            auto_recharge_threshold = self.auto_recharge_threshold

        auto_recharge_amount: int | None | Unset
        if isinstance(self.auto_recharge_amount, Unset):
            auto_recharge_amount = UNSET
        else:
            auto_recharge_amount = self.auto_recharge_amount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auto_recharge_threshold is not UNSET:
            field_dict["auto_recharge_threshold"] = auto_recharge_threshold
        if auto_recharge_amount is not UNSET:
            field_dict["auto_recharge_amount"] = auto_recharge_amount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_auto_recharge_threshold(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        auto_recharge_threshold = _parse_auto_recharge_threshold(d.pop("auto_recharge_threshold", UNSET))

        def _parse_auto_recharge_amount(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        auto_recharge_amount = _parse_auto_recharge_amount(d.pop("auto_recharge_amount", UNSET))

        update_wallet_auto_recharge_body = cls(
            auto_recharge_threshold=auto_recharge_threshold,
            auto_recharge_amount=auto_recharge_amount,
        )

        update_wallet_auto_recharge_body.additional_properties = d
        return update_wallet_auto_recharge_body

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
