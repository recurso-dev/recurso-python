from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_gstr3b_response_200_data import GetGSTR3BResponse200Data
    from ..models.get_gstr3b_response_200_gov_schema import GetGSTR3BResponse200GovSchema


T = TypeVar("T", bound="GetGSTR3BResponse200")


@_attrs_define
class GetGSTR3BResponse200:
    """
    Attributes:
        data (GetGSTR3BResponse200Data | Unset): Readable GSTR-3B sections (amounts in minor units).
        gov_schema (GetGSTR3BResponse200GovSchema | Unset): GSTN GSTR-3B upload JSON (official field names, amounts in
            rupees).
    """

    data: GetGSTR3BResponse200Data | Unset = UNSET
    gov_schema: GetGSTR3BResponse200GovSchema | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        gov_schema: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gov_schema, Unset):
            gov_schema = self.gov_schema.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if gov_schema is not UNSET:
            field_dict["gov_schema"] = gov_schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_gstr3b_response_200_data import GetGSTR3BResponse200Data
        from ..models.get_gstr3b_response_200_gov_schema import GetGSTR3BResponse200GovSchema

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: GetGSTR3BResponse200Data | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = GetGSTR3BResponse200Data.from_dict(_data)

        _gov_schema = d.pop("gov_schema", UNSET)
        gov_schema: GetGSTR3BResponse200GovSchema | Unset
        if isinstance(_gov_schema, Unset):
            gov_schema = UNSET
        else:
            gov_schema = GetGSTR3BResponse200GovSchema.from_dict(_gov_schema)

        get_gstr3b_response_200 = cls(
            data=data,
            gov_schema=gov_schema,
        )

        get_gstr3b_response_200.additional_properties = d
        return get_gstr3b_response_200

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
