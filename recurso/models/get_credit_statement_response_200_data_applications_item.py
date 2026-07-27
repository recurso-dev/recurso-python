from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetCreditStatementResponse200DataApplicationsItem")


@_attrs_define
class GetCreditStatementResponse200DataApplicationsItem:
    """
    Attributes:
        credit_note_id (UUID | Unset):
        invoice_id (UUID | Unset):
        invoice_number (str | Unset):
        currency (str | Unset):
        amount (int | Unset):
        created_at (datetime.datetime | Unset):
    """

    credit_note_id: UUID | Unset = UNSET
    invoice_id: UUID | Unset = UNSET
    invoice_number: str | Unset = UNSET
    currency: str | Unset = UNSET
    amount: int | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        credit_note_id: str | Unset = UNSET
        if not isinstance(self.credit_note_id, Unset):
            credit_note_id = str(self.credit_note_id)

        invoice_id: str | Unset = UNSET
        if not isinstance(self.invoice_id, Unset):
            invoice_id = str(self.invoice_id)

        invoice_number = self.invoice_number

        currency = self.currency

        amount = self.amount

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if credit_note_id is not UNSET:
            field_dict["credit_note_id"] = credit_note_id
        if invoice_id is not UNSET:
            field_dict["invoice_id"] = invoice_id
        if invoice_number is not UNSET:
            field_dict["invoice_number"] = invoice_number
        if currency is not UNSET:
            field_dict["currency"] = currency
        if amount is not UNSET:
            field_dict["amount"] = amount
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _credit_note_id = d.pop("credit_note_id", UNSET)
        credit_note_id: UUID | Unset
        if isinstance(_credit_note_id, Unset):
            credit_note_id = UNSET
        else:
            credit_note_id = UUID(_credit_note_id)

        _invoice_id = d.pop("invoice_id", UNSET)
        invoice_id: UUID | Unset
        if isinstance(_invoice_id, Unset):
            invoice_id = UNSET
        else:
            invoice_id = UUID(_invoice_id)

        invoice_number = d.pop("invoice_number", UNSET)

        currency = d.pop("currency", UNSET)

        amount = d.pop("amount", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        get_credit_statement_response_200_data_applications_item = cls(
            credit_note_id=credit_note_id,
            invoice_id=invoice_id,
            invoice_number=invoice_number,
            currency=currency,
            amount=amount,
            created_at=created_at,
        )

        get_credit_statement_response_200_data_applications_item.additional_properties = d
        return get_credit_statement_response_200_data_applications_item

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
