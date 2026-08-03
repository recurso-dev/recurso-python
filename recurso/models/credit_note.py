from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.credit_note_status import CreditNoteStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.customer import Customer


T = TypeVar("T", bound="CreditNote")


@_attrs_define
class CreditNote:
    """
    Attributes:
        id (UUID | Unset):
        tenant_id (UUID | Unset):
        customer_id (UUID | Unset):
        invoice_id (None | Unset | UUID):
        entity_id (None | Unset | UUID): Legal entity that issued the credit note (Multi-Entity Books); inherits the
            referenced invoice's entity.
        reference (None | str | Unset):
        amount (int | Unset):
        subtotal (int | Unset): Taxable (net-of-tax) value of the credit, minor units. Present (non-zero) when the note
            recorded a tax breakdown at creation — invoice-linked credits slice the invoice's tax proportionally, downgrade
            credits carry the reversed proration tax. 0 on legacy rows and standalone goodwill credits (gross-only).
        tax_amount (int | Unset): Tax reversed by this credit, minor units.
        igst_amount (int | Unset):
        cgst_amount (int | Unset):
        sgst_amount (int | Unset):
        tax_type (str | Unset): Tax regime of the breakdown (e.g. inter_state, intra_state); empty when none recorded.
        hsn_code (str | Unset):
        balance (int | Unset): Remaining unapplied credit.
        currency (str | Unset):
        status (CreditNoteStatus | Unset):
        reason (str | Unset):
        expires_at (datetime.datetime | None | Unset): When a dated adjustment credit lapses; null = never expires.
        created_at (datetime.datetime | Unset):
        updated_at (datetime.datetime | Unset):
        customer (Customer | Unset):
    """

    id: UUID | Unset = UNSET
    tenant_id: UUID | Unset = UNSET
    customer_id: UUID | Unset = UNSET
    invoice_id: None | Unset | UUID = UNSET
    entity_id: None | Unset | UUID = UNSET
    reference: None | str | Unset = UNSET
    amount: int | Unset = UNSET
    subtotal: int | Unset = UNSET
    tax_amount: int | Unset = UNSET
    igst_amount: int | Unset = UNSET
    cgst_amount: int | Unset = UNSET
    sgst_amount: int | Unset = UNSET
    tax_type: str | Unset = UNSET
    hsn_code: str | Unset = UNSET
    balance: int | Unset = UNSET
    currency: str | Unset = UNSET
    status: CreditNoteStatus | Unset = UNSET
    reason: str | Unset = UNSET
    expires_at: datetime.datetime | None | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    customer: Customer | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        tenant_id: str | Unset = UNSET
        if not isinstance(self.tenant_id, Unset):
            tenant_id = str(self.tenant_id)

        customer_id: str | Unset = UNSET
        if not isinstance(self.customer_id, Unset):
            customer_id = str(self.customer_id)

        invoice_id: None | str | Unset
        if isinstance(self.invoice_id, Unset):
            invoice_id = UNSET
        elif isinstance(self.invoice_id, UUID):
            invoice_id = str(self.invoice_id)
        else:
            invoice_id = self.invoice_id

        entity_id: None | str | Unset
        if isinstance(self.entity_id, Unset):
            entity_id = UNSET
        elif isinstance(self.entity_id, UUID):
            entity_id = str(self.entity_id)
        else:
            entity_id = self.entity_id

        reference: None | str | Unset
        if isinstance(self.reference, Unset):
            reference = UNSET
        else:
            reference = self.reference

        amount = self.amount

        subtotal = self.subtotal

        tax_amount = self.tax_amount

        igst_amount = self.igst_amount

        cgst_amount = self.cgst_amount

        sgst_amount = self.sgst_amount

        tax_type = self.tax_type

        hsn_code = self.hsn_code

        balance = self.balance

        currency = self.currency

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        reason = self.reason

        expires_at: None | str | Unset
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        elif isinstance(self.expires_at, datetime.datetime):
            expires_at = self.expires_at.isoformat()
        else:
            expires_at = self.expires_at

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        customer: dict[str, Any] | Unset = UNSET
        if not isinstance(self.customer, Unset):
            customer = self.customer.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if tenant_id is not UNSET:
            field_dict["tenant_id"] = tenant_id
        if customer_id is not UNSET:
            field_dict["customer_id"] = customer_id
        if invoice_id is not UNSET:
            field_dict["invoice_id"] = invoice_id
        if entity_id is not UNSET:
            field_dict["entity_id"] = entity_id
        if reference is not UNSET:
            field_dict["reference"] = reference
        if amount is not UNSET:
            field_dict["amount"] = amount
        if subtotal is not UNSET:
            field_dict["subtotal"] = subtotal
        if tax_amount is not UNSET:
            field_dict["tax_amount"] = tax_amount
        if igst_amount is not UNSET:
            field_dict["igst_amount"] = igst_amount
        if cgst_amount is not UNSET:
            field_dict["cgst_amount"] = cgst_amount
        if sgst_amount is not UNSET:
            field_dict["sgst_amount"] = sgst_amount
        if tax_type is not UNSET:
            field_dict["tax_type"] = tax_type
        if hsn_code is not UNSET:
            field_dict["hsn_code"] = hsn_code
        if balance is not UNSET:
            field_dict["balance"] = balance
        if currency is not UNSET:
            field_dict["currency"] = currency
        if status is not UNSET:
            field_dict["status"] = status
        if reason is not UNSET:
            field_dict["reason"] = reason
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if customer is not UNSET:
            field_dict["customer"] = customer

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.customer import Customer

        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        _tenant_id = d.pop("tenant_id", UNSET)
        tenant_id: UUID | Unset
        if isinstance(_tenant_id, Unset):
            tenant_id = UNSET
        else:
            tenant_id = UUID(_tenant_id)

        _customer_id = d.pop("customer_id", UNSET)
        customer_id: UUID | Unset
        if isinstance(_customer_id, Unset):
            customer_id = UNSET
        else:
            customer_id = UUID(_customer_id)

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

        def _parse_entity_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                entity_id_type_0 = UUID(data)

                return entity_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        entity_id = _parse_entity_id(d.pop("entity_id", UNSET))

        def _parse_reference(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reference = _parse_reference(d.pop("reference", UNSET))

        amount = d.pop("amount", UNSET)

        subtotal = d.pop("subtotal", UNSET)

        tax_amount = d.pop("tax_amount", UNSET)

        igst_amount = d.pop("igst_amount", UNSET)

        cgst_amount = d.pop("cgst_amount", UNSET)

        sgst_amount = d.pop("sgst_amount", UNSET)

        tax_type = d.pop("tax_type", UNSET)

        hsn_code = d.pop("hsn_code", UNSET)

        balance = d.pop("balance", UNSET)

        currency = d.pop("currency", UNSET)

        _status = d.pop("status", UNSET)
        status: CreditNoteStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CreditNoteStatus(_status)

        reason = d.pop("reason", UNSET)

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

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = datetime.datetime.fromisoformat(_updated_at)

        _customer = d.pop("customer", UNSET)
        customer: Customer | Unset
        if isinstance(_customer, Unset):
            customer = UNSET
        else:
            customer = Customer.from_dict(_customer)

        credit_note = cls(
            id=id,
            tenant_id=tenant_id,
            customer_id=customer_id,
            invoice_id=invoice_id,
            entity_id=entity_id,
            reference=reference,
            amount=amount,
            subtotal=subtotal,
            tax_amount=tax_amount,
            igst_amount=igst_amount,
            cgst_amount=cgst_amount,
            sgst_amount=sgst_amount,
            tax_type=tax_type,
            hsn_code=hsn_code,
            balance=balance,
            currency=currency,
            status=status,
            reason=reason,
            expires_at=expires_at,
            created_at=created_at,
            updated_at=updated_at,
            customer=customer,
        )

        credit_note.additional_properties = d
        return credit_note

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
