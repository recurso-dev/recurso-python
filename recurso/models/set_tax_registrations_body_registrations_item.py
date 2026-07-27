from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.set_tax_registrations_body_registrations_item_status import SetTaxRegistrationsBodyRegistrationsItemStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="SetTaxRegistrationsBodyRegistrationsItem")


@_attrs_define
class SetTaxRegistrationsBodyRegistrationsItem:
    """
    Attributes:
        state_code (str):  Example: CA.
        registration_number (str | Unset):
        status (SetTaxRegistrationsBodyRegistrationsItemStatus | Unset):  Default:
            SetTaxRegistrationsBodyRegistrationsItemStatus.REGISTERED.
        registered_at (datetime.date | Unset):
    """

    state_code: str
    registration_number: str | Unset = UNSET
    status: SetTaxRegistrationsBodyRegistrationsItemStatus | Unset = (
        SetTaxRegistrationsBodyRegistrationsItemStatus.REGISTERED
    )
    registered_at: datetime.date | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        state_code = self.state_code

        registration_number = self.registration_number

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        registered_at: str | Unset = UNSET
        if not isinstance(self.registered_at, Unset):
            registered_at = self.registered_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "state_code": state_code,
            }
        )
        if registration_number is not UNSET:
            field_dict["registration_number"] = registration_number
        if status is not UNSET:
            field_dict["status"] = status
        if registered_at is not UNSET:
            field_dict["registered_at"] = registered_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        state_code = d.pop("state_code")

        registration_number = d.pop("registration_number", UNSET)

        _status = d.pop("status", UNSET)
        status: SetTaxRegistrationsBodyRegistrationsItemStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = SetTaxRegistrationsBodyRegistrationsItemStatus(_status)

        _registered_at = d.pop("registered_at", UNSET)
        registered_at: datetime.date | Unset
        if isinstance(_registered_at, Unset):
            registered_at = UNSET
        else:
            registered_at = datetime.date.fromisoformat(_registered_at)

        set_tax_registrations_body_registrations_item = cls(
            state_code=state_code,
            registration_number=registration_number,
            status=status,
            registered_at=registered_at,
        )

        set_tax_registrations_body_registrations_item.additional_properties = d
        return set_tax_registrations_body_registrations_item

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
