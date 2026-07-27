from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.collections_queue_item_managed_by import CollectionsQueueItemManagedBy
from ..models.collections_queue_item_status import CollectionsQueueItemStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="CollectionsQueueItem")


@_attrs_define
class CollectionsQueueItem:
    """One currently-failing invoice on the collections worklist.

    Attributes:
        id (UUID | Unset):
        customer_id (UUID | Unset):
        customer_name (str | Unset):
        customer_email (str | Unset):
        invoice_number (str | Unset):
        status (CollectionsQueueItemStatus | Unset):
        currency (str | Unset):
        amount_remaining (int | Unset): Total minus amount paid, in minor units.
        due_date (datetime.datetime | Unset):
        days_overdue (int | Unset):
        retry_count (int | Unset):
        last_payment_error (str | Unset): Raw gateway/ACH failure code from the last attempt, if any.
        next_retry_at (datetime.datetime | None | Unset):
        managed_by (CollectionsQueueItemManagedBy | Unset):
        attempt_status (str | Unset): Status of the latest payment attempt (ACH), if one exists.
    """

    id: UUID | Unset = UNSET
    customer_id: UUID | Unset = UNSET
    customer_name: str | Unset = UNSET
    customer_email: str | Unset = UNSET
    invoice_number: str | Unset = UNSET
    status: CollectionsQueueItemStatus | Unset = UNSET
    currency: str | Unset = UNSET
    amount_remaining: int | Unset = UNSET
    due_date: datetime.datetime | Unset = UNSET
    days_overdue: int | Unset = UNSET
    retry_count: int | Unset = UNSET
    last_payment_error: str | Unset = UNSET
    next_retry_at: datetime.datetime | None | Unset = UNSET
    managed_by: CollectionsQueueItemManagedBy | Unset = UNSET
    attempt_status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        customer_id: str | Unset = UNSET
        if not isinstance(self.customer_id, Unset):
            customer_id = str(self.customer_id)

        customer_name = self.customer_name

        customer_email = self.customer_email

        invoice_number = self.invoice_number

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        currency = self.currency

        amount_remaining = self.amount_remaining

        due_date: str | Unset = UNSET
        if not isinstance(self.due_date, Unset):
            due_date = self.due_date.isoformat()

        days_overdue = self.days_overdue

        retry_count = self.retry_count

        last_payment_error = self.last_payment_error

        next_retry_at: None | str | Unset
        if isinstance(self.next_retry_at, Unset):
            next_retry_at = UNSET
        elif isinstance(self.next_retry_at, datetime.datetime):
            next_retry_at = self.next_retry_at.isoformat()
        else:
            next_retry_at = self.next_retry_at

        managed_by: str | Unset = UNSET
        if not isinstance(self.managed_by, Unset):
            managed_by = self.managed_by.value

        attempt_status = self.attempt_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if customer_id is not UNSET:
            field_dict["customer_id"] = customer_id
        if customer_name is not UNSET:
            field_dict["customer_name"] = customer_name
        if customer_email is not UNSET:
            field_dict["customer_email"] = customer_email
        if invoice_number is not UNSET:
            field_dict["invoice_number"] = invoice_number
        if status is not UNSET:
            field_dict["status"] = status
        if currency is not UNSET:
            field_dict["currency"] = currency
        if amount_remaining is not UNSET:
            field_dict["amount_remaining"] = amount_remaining
        if due_date is not UNSET:
            field_dict["due_date"] = due_date
        if days_overdue is not UNSET:
            field_dict["days_overdue"] = days_overdue
        if retry_count is not UNSET:
            field_dict["retry_count"] = retry_count
        if last_payment_error is not UNSET:
            field_dict["last_payment_error"] = last_payment_error
        if next_retry_at is not UNSET:
            field_dict["next_retry_at"] = next_retry_at
        if managed_by is not UNSET:
            field_dict["managed_by"] = managed_by
        if attempt_status is not UNSET:
            field_dict["attempt_status"] = attempt_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        _customer_id = d.pop("customer_id", UNSET)
        customer_id: UUID | Unset
        if isinstance(_customer_id, Unset):
            customer_id = UNSET
        else:
            customer_id = UUID(_customer_id)

        customer_name = d.pop("customer_name", UNSET)

        customer_email = d.pop("customer_email", UNSET)

        invoice_number = d.pop("invoice_number", UNSET)

        _status = d.pop("status", UNSET)
        status: CollectionsQueueItemStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CollectionsQueueItemStatus(_status)

        currency = d.pop("currency", UNSET)

        amount_remaining = d.pop("amount_remaining", UNSET)

        _due_date = d.pop("due_date", UNSET)
        due_date: datetime.datetime | Unset
        if isinstance(_due_date, Unset):
            due_date = UNSET
        else:
            due_date = datetime.datetime.fromisoformat(_due_date)

        days_overdue = d.pop("days_overdue", UNSET)

        retry_count = d.pop("retry_count", UNSET)

        last_payment_error = d.pop("last_payment_error", UNSET)

        def _parse_next_retry_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_retry_at_type_0 = datetime.datetime.fromisoformat(data)

                return next_retry_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        next_retry_at = _parse_next_retry_at(d.pop("next_retry_at", UNSET))

        _managed_by = d.pop("managed_by", UNSET)
        managed_by: CollectionsQueueItemManagedBy | Unset
        if isinstance(_managed_by, Unset):
            managed_by = UNSET
        else:
            managed_by = CollectionsQueueItemManagedBy(_managed_by)

        attempt_status = d.pop("attempt_status", UNSET)

        collections_queue_item = cls(
            id=id,
            customer_id=customer_id,
            customer_name=customer_name,
            customer_email=customer_email,
            invoice_number=invoice_number,
            status=status,
            currency=currency,
            amount_remaining=amount_remaining,
            due_date=due_date,
            days_overdue=days_overdue,
            retry_count=retry_count,
            last_payment_error=last_payment_error,
            next_retry_at=next_retry_at,
            managed_by=managed_by,
            attempt_status=attempt_status,
        )

        collections_queue_item.additional_properties = d
        return collections_queue_item

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
