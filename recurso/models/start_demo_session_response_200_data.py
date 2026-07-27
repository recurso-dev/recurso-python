from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StartDemoSessionResponse200Data")


@_attrs_define
class StartDemoSessionResponse200Data:
    """
    Attributes:
        demo (bool | Unset):
        email (str | Unset):
        api_key (str | Unset):
    """

    demo: bool | Unset = UNSET
    email: str | Unset = UNSET
    api_key: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        demo = self.demo

        email = self.email

        api_key = self.api_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if demo is not UNSET:
            field_dict["demo"] = demo
        if email is not UNSET:
            field_dict["email"] = email
        if api_key is not UNSET:
            field_dict["api_key"] = api_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        demo = d.pop("demo", UNSET)

        email = d.pop("email", UNSET)

        api_key = d.pop("api_key", UNSET)

        start_demo_session_response_200_data = cls(
            demo=demo,
            email=email,
            api_key=api_key,
        )

        start_demo_session_response_200_data.additional_properties = d
        return start_demo_session_response_200_data

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
