from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.retry_eue_invoice_response_200_data_type_0 import RetryEUEInvoiceResponse200DataType0





T = TypeVar("T", bound="RetryEUEInvoiceResponse200")



@_attrs_define
class RetryEUEInvoiceResponse200:
    """ 
        Attributes:
            data (None | RetryEUEInvoiceResponse200DataType0 | Unset):
            message (str | Unset):
     """

    data: None | RetryEUEInvoiceResponse200DataType0 | Unset = UNSET
    message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.retry_eue_invoice_response_200_data_type_0 import RetryEUEInvoiceResponse200DataType0
        data: dict[str, Any] | None | Unset
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, RetryEUEInvoiceResponse200DataType0):
            data = self.data.to_dict()
        else:
            data = self.data

        message = self.message


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if data is not UNSET:
            field_dict["data"] = data
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.retry_eue_invoice_response_200_data_type_0 import RetryEUEInvoiceResponse200DataType0
        d = dict(src_dict)
        def _parse_data(data: object) -> None | RetryEUEInvoiceResponse200DataType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = RetryEUEInvoiceResponse200DataType0.from_dict(data)



                return data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RetryEUEInvoiceResponse200DataType0 | Unset, data)

        data = _parse_data(d.pop("data", UNSET))


        message = d.pop("message", UNSET)

        retry_eue_invoice_response_200 = cls(
            data=data,
            message=message,
        )


        retry_eue_invoice_response_200.additional_properties = d
        return retry_eue_invoice_response_200

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
