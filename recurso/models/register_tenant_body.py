from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RegisterTenantBody")


@_attrs_define
class RegisterTenantBody:
    """
    Attributes:
        company_name (str): The tenant / company name.
        name (str): The owner user's display name.
        email (str):
        password (str):
        country (str | Unset): Optional ISO-2 business country (e.g. "US"). Stamped on the tenant's primary legal
            entity, which is the seller tax jurisdiction — a US signup invoices under US sales tax from day one. Omit to
            configure later in settings.
    """

    company_name: str
    name: str
    email: str
    password: str
    country: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company_name = self.company_name

        name = self.name

        email = self.email

        password = self.password

        country = self.country

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "company_name": company_name,
                "name": name,
                "email": email,
                "password": password,
            }
        )
        if country is not UNSET:
            field_dict["country"] = country

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        company_name = d.pop("company_name")

        name = d.pop("name")

        email = d.pop("email")

        password = d.pop("password")

        country = d.pop("country", UNSET)

        register_tenant_body = cls(
            company_name=company_name,
            name=name,
            email=email,
            password=password,
            country=country,
        )

        register_tenant_body.additional_properties = d
        return register_tenant_body

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
