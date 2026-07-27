from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.create_customer_request_tax_type import CreateCustomerRequestTaxType
from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="CreateCustomerRequest")



@_attrs_define
class CreateCustomerRequest:
    """ 
        Attributes:
            email (str):
            name (str):
            phone (str | Unset):
            tax_id (str | Unset):
            gstin (str | Unset): Indian GST identification number (B2B customers).
            tax_type (CreateCustomerRequestTaxType | Unset):
            place_of_supply (str | Unset): Indian state code for GST place of supply.
            tax_exempt (bool | Unset): US sales-tax exemption status (D2). When true, the number and code are passed to the
                tax provider.
            tax_exemption_number (str | Unset): Exemption/resale certificate number on file.
            tax_exemption_code (str | Unset): Provider entity-use / customer-usage code (e.g. Avalara "A"); also the
                exemption reason.
            tax_exemption_expires_at (datetime.date | None | Unset): Exemption certificate expiry (YYYY-MM-DD). Honored
                through this date; past it the buyer is charged tax again. Null = no expiry on file (Inc 2).
            line1 (str | Unset):
            city (str | Unset):
            state (str | Unset):
            zip_ (str | Unset):
            country (str | Unset): ISO 3166-1 alpha-2 code.
     """

    email: str
    name: str
    phone: str | Unset = UNSET
    tax_id: str | Unset = UNSET
    gstin: str | Unset = UNSET
    tax_type: CreateCustomerRequestTaxType | Unset = UNSET
    place_of_supply: str | Unset = UNSET
    tax_exempt: bool | Unset = UNSET
    tax_exemption_number: str | Unset = UNSET
    tax_exemption_code: str | Unset = UNSET
    tax_exemption_expires_at: datetime.date | None | Unset = UNSET
    line1: str | Unset = UNSET
    city: str | Unset = UNSET
    state: str | Unset = UNSET
    zip_: str | Unset = UNSET
    country: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        email = self.email

        name = self.name

        phone = self.phone

        tax_id = self.tax_id

        gstin = self.gstin

        tax_type: str | Unset = UNSET
        if not isinstance(self.tax_type, Unset):
            tax_type = self.tax_type.value


        place_of_supply = self.place_of_supply

        tax_exempt = self.tax_exempt

        tax_exemption_number = self.tax_exemption_number

        tax_exemption_code = self.tax_exemption_code

        tax_exemption_expires_at: None | str | Unset
        if isinstance(self.tax_exemption_expires_at, Unset):
            tax_exemption_expires_at = UNSET
        elif isinstance(self.tax_exemption_expires_at, datetime.date):
            tax_exemption_expires_at = self.tax_exemption_expires_at.isoformat()
        else:
            tax_exemption_expires_at = self.tax_exemption_expires_at

        line1 = self.line1

        city = self.city

        state = self.state

        zip_ = self.zip_

        country = self.country


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "email": email,
            "name": name,
        })
        if phone is not UNSET:
            field_dict["phone"] = phone
        if tax_id is not UNSET:
            field_dict["tax_id"] = tax_id
        if gstin is not UNSET:
            field_dict["gstin"] = gstin
        if tax_type is not UNSET:
            field_dict["tax_type"] = tax_type
        if place_of_supply is not UNSET:
            field_dict["place_of_supply"] = place_of_supply
        if tax_exempt is not UNSET:
            field_dict["tax_exempt"] = tax_exempt
        if tax_exemption_number is not UNSET:
            field_dict["tax_exemption_number"] = tax_exemption_number
        if tax_exemption_code is not UNSET:
            field_dict["tax_exemption_code"] = tax_exemption_code
        if tax_exemption_expires_at is not UNSET:
            field_dict["tax_exemption_expires_at"] = tax_exemption_expires_at
        if line1 is not UNSET:
            field_dict["line1"] = line1
        if city is not UNSET:
            field_dict["city"] = city
        if state is not UNSET:
            field_dict["state"] = state
        if zip_ is not UNSET:
            field_dict["zip"] = zip_
        if country is not UNSET:
            field_dict["country"] = country

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email")

        name = d.pop("name")

        phone = d.pop("phone", UNSET)

        tax_id = d.pop("tax_id", UNSET)

        gstin = d.pop("gstin", UNSET)

        _tax_type = d.pop("tax_type", UNSET)
        tax_type: CreateCustomerRequestTaxType | Unset
        if isinstance(_tax_type,  Unset):
            tax_type = UNSET
        else:
            tax_type = CreateCustomerRequestTaxType(_tax_type)




        place_of_supply = d.pop("place_of_supply", UNSET)

        tax_exempt = d.pop("tax_exempt", UNSET)

        tax_exemption_number = d.pop("tax_exemption_number", UNSET)

        tax_exemption_code = d.pop("tax_exemption_code", UNSET)

        def _parse_tax_exemption_expires_at(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                tax_exemption_expires_at_type_0 = datetime.date.fromisoformat(data)



                return tax_exemption_expires_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        tax_exemption_expires_at = _parse_tax_exemption_expires_at(d.pop("tax_exemption_expires_at", UNSET))


        line1 = d.pop("line1", UNSET)

        city = d.pop("city", UNSET)

        state = d.pop("state", UNSET)

        zip_ = d.pop("zip", UNSET)

        country = d.pop("country", UNSET)

        create_customer_request = cls(
            email=email,
            name=name,
            phone=phone,
            tax_id=tax_id,
            gstin=gstin,
            tax_type=tax_type,
            place_of_supply=place_of_supply,
            tax_exempt=tax_exempt,
            tax_exemption_number=tax_exemption_number,
            tax_exemption_code=tax_exemption_code,
            tax_exemption_expires_at=tax_exemption_expires_at,
            line1=line1,
            city=city,
            state=state,
            zip_=zip_,
            country=country,
        )


        create_customer_request.additional_properties = d
        return create_customer_request

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
