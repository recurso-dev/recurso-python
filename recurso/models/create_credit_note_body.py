from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.create_credit_note_body_type import CreateCreditNoteBodyType
from ..types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime






T = TypeVar("T", bound="CreateCreditNoteBody")



@_attrs_define
class CreateCreditNoteBody:
    """ 
        Attributes:
            customer_id (UUID):
            amount (int): Amount in the lowest currency unit.
            currency (str):
            invoice_id (None | Unset | UUID):
            reason (str | Unset):
            type_ (CreateCreditNoteBodyType | Unset): `adjustment` (default) issues account credit. `refund` calls the
                gateway's refund API against the paid invoice in `invoice_id` and posts a Refunds-vs-Cash ledger reversal; its
                progress is tracked by the credit note's `refund_status`. Default: CreateCreditNoteBodyType.ADJUSTMENT.
            expires_at (datetime.datetime | None | Unset): Optional expiry for a spendable adjustment credit. When it passes
                with balance remaining, the expiry sweep writes the balance off (DR Customer Credit / CR Credits & Adjustments).
                Ignored for refunds.
     """

    customer_id: UUID
    amount: int
    currency: str
    invoice_id: None | Unset | UUID = UNSET
    reason: str | Unset = UNSET
    type_: CreateCreditNoteBodyType | Unset = CreateCreditNoteBodyType.ADJUSTMENT
    expires_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        customer_id = str(self.customer_id)

        amount = self.amount

        currency = self.currency

        invoice_id: None | str | Unset
        if isinstance(self.invoice_id, Unset):
            invoice_id = UNSET
        elif isinstance(self.invoice_id, UUID):
            invoice_id = str(self.invoice_id)
        else:
            invoice_id = self.invoice_id

        reason = self.reason

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value


        expires_at: None | str | Unset
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        elif isinstance(self.expires_at, datetime.datetime):
            expires_at = self.expires_at.isoformat()
        else:
            expires_at = self.expires_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "customer_id": customer_id,
            "amount": amount,
            "currency": currency,
        })
        if invoice_id is not UNSET:
            field_dict["invoice_id"] = invoice_id
        if reason is not UNSET:
            field_dict["reason"] = reason
        if type_ is not UNSET:
            field_dict["type"] = type_
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        customer_id = UUID(d.pop("customer_id"))




        amount = d.pop("amount")

        currency = d.pop("currency")

        def _parse_invoice_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                invoice_id_type_0 = UUID(data)



                return invoice_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        invoice_id = _parse_invoice_id(d.pop("invoice_id", UNSET))


        reason = d.pop("reason", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: CreateCreditNoteBodyType | Unset
        if isinstance(_type_,  Unset):
            type_ = UNSET
        else:
            type_ = CreateCreditNoteBodyType(_type_)




        def _parse_expires_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_at_type_0 = datetime.datetime.fromisoformat(data)



                return expires_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        expires_at = _parse_expires_at(d.pop("expires_at", UNSET))


        create_credit_note_body = cls(
            customer_id=customer_id,
            amount=amount,
            currency=currency,
            invoice_id=invoice_id,
            reason=reason,
            type_=type_,
            expires_at=expires_at,
        )


        create_credit_note_body.additional_properties = d
        return create_credit_note_body

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
