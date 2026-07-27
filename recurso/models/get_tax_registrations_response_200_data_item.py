from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_tax_registrations_response_200_data_item_status import GetTaxRegistrationsResponse200DataItemStatus
from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="GetTaxRegistrationsResponse200DataItem")



@_attrs_define
class GetTaxRegistrationsResponse200DataItem:
    """ 
        Attributes:
            state_code (str | Unset):
            registration_number (str | Unset):
            status (GetTaxRegistrationsResponse200DataItemStatus | Unset):
            registered_at (datetime.date | None | Unset):
     """

    state_code: str | Unset = UNSET
    registration_number: str | Unset = UNSET
    status: GetTaxRegistrationsResponse200DataItemStatus | Unset = UNSET
    registered_at: datetime.date | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        state_code = self.state_code

        registration_number = self.registration_number

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        registered_at: None | str | Unset
        if isinstance(self.registered_at, Unset):
            registered_at = UNSET
        elif isinstance(self.registered_at, datetime.date):
            registered_at = self.registered_at.isoformat()
        else:
            registered_at = self.registered_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if state_code is not UNSET:
            field_dict["state_code"] = state_code
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
        state_code = d.pop("state_code", UNSET)

        registration_number = d.pop("registration_number", UNSET)

        _status = d.pop("status", UNSET)
        status: GetTaxRegistrationsResponse200DataItemStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = GetTaxRegistrationsResponse200DataItemStatus(_status)




        def _parse_registered_at(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                registered_at_type_0 = datetime.date.fromisoformat(data)



                return registered_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        registered_at = _parse_registered_at(d.pop("registered_at", UNSET))


        get_tax_registrations_response_200_data_item = cls(
            state_code=state_code,
            registration_number=registration_number,
            status=status,
            registered_at=registered_at,
        )


        get_tax_registrations_response_200_data_item.additional_properties = d
        return get_tax_registrations_response_200_data_item

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
