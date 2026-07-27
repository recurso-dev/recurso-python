from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.set_tax_registrations_body_registrations_item import SetTaxRegistrationsBodyRegistrationsItem


T = TypeVar("T", bound="SetTaxRegistrationsBody")


@_attrs_define
class SetTaxRegistrationsBody:
    """
    Attributes:
        registrations (list[SetTaxRegistrationsBodyRegistrationsItem] | Unset):
    """

    registrations: list[SetTaxRegistrationsBodyRegistrationsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        registrations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.registrations, Unset):
            registrations = []
            for registrations_item_data in self.registrations:
                registrations_item = registrations_item_data.to_dict()
                registrations.append(registrations_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if registrations is not UNSET:
            field_dict["registrations"] = registrations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.set_tax_registrations_body_registrations_item import SetTaxRegistrationsBodyRegistrationsItem

        d = dict(src_dict)
        _registrations = d.pop("registrations", UNSET)
        registrations: list[SetTaxRegistrationsBodyRegistrationsItem] | Unset = UNSET
        if _registrations is not UNSET:
            registrations = []
            for registrations_item_data in _registrations:
                registrations_item = SetTaxRegistrationsBodyRegistrationsItem.from_dict(registrations_item_data)

                registrations.append(registrations_item)

        set_tax_registrations_body = cls(
            registrations=registrations,
        )

        set_tax_registrations_body.additional_properties = d
        return set_tax_registrations_body

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
