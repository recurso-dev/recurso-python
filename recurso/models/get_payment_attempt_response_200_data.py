from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_payment_attempt_response_200_data_status import GetPaymentAttemptResponse200DataStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetPaymentAttemptResponse200Data")


@_attrs_define
class GetPaymentAttemptResponse200Data:
    """
    Attributes:
        id (UUID | Unset):
        invoice_id (UUID | Unset):
        invoice_number (str | Unset):
        currency (str | Unset):
        customer_id (UUID | Unset):
        subscription_id (None | Unset | UUID):
        gateway (str | Unset):
        method (str | Unset):
        gateway_payment_intent_id (str | Unset):
        status (GetPaymentAttemptResponse200DataStatus | Unset):
        failure_code (str | Unset):
        amount (int | Unset):
        created_at (datetime.datetime | Unset):
        updated_at (datetime.datetime | Unset):
        settled_at (datetime.datetime | None | Unset):
    """

    id: UUID | Unset = UNSET
    invoice_id: UUID | Unset = UNSET
    invoice_number: str | Unset = UNSET
    currency: str | Unset = UNSET
    customer_id: UUID | Unset = UNSET
    subscription_id: None | Unset | UUID = UNSET
    gateway: str | Unset = UNSET
    method: str | Unset = UNSET
    gateway_payment_intent_id: str | Unset = UNSET
    status: GetPaymentAttemptResponse200DataStatus | Unset = UNSET
    failure_code: str | Unset = UNSET
    amount: int | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    settled_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        invoice_id: str | Unset = UNSET
        if not isinstance(self.invoice_id, Unset):
            invoice_id = str(self.invoice_id)

        invoice_number = self.invoice_number

        currency = self.currency

        customer_id: str | Unset = UNSET
        if not isinstance(self.customer_id, Unset):
            customer_id = str(self.customer_id)

        subscription_id: None | str | Unset
        if isinstance(self.subscription_id, Unset):
            subscription_id = UNSET
        elif isinstance(self.subscription_id, UUID):
            subscription_id = str(self.subscription_id)
        else:
            subscription_id = self.subscription_id

        gateway = self.gateway

        method = self.method

        gateway_payment_intent_id = self.gateway_payment_intent_id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        failure_code = self.failure_code

        amount = self.amount

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        settled_at: None | str | Unset
        if isinstance(self.settled_at, Unset):
            settled_at = UNSET
        elif isinstance(self.settled_at, datetime.datetime):
            settled_at = self.settled_at.isoformat()
        else:
            settled_at = self.settled_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if invoice_id is not UNSET:
            field_dict["invoice_id"] = invoice_id
        if invoice_number is not UNSET:
            field_dict["invoice_number"] = invoice_number
        if currency is not UNSET:
            field_dict["currency"] = currency
        if customer_id is not UNSET:
            field_dict["customer_id"] = customer_id
        if subscription_id is not UNSET:
            field_dict["subscription_id"] = subscription_id
        if gateway is not UNSET:
            field_dict["gateway"] = gateway
        if method is not UNSET:
            field_dict["method"] = method
        if gateway_payment_intent_id is not UNSET:
            field_dict["gateway_payment_intent_id"] = gateway_payment_intent_id
        if status is not UNSET:
            field_dict["status"] = status
        if failure_code is not UNSET:
            field_dict["failure_code"] = failure_code
        if amount is not UNSET:
            field_dict["amount"] = amount
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if settled_at is not UNSET:
            field_dict["settled_at"] = settled_at

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

        _invoice_id = d.pop("invoice_id", UNSET)
        invoice_id: UUID | Unset
        if isinstance(_invoice_id, Unset):
            invoice_id = UNSET
        else:
            invoice_id = UUID(_invoice_id)

        invoice_number = d.pop("invoice_number", UNSET)

        currency = d.pop("currency", UNSET)

        _customer_id = d.pop("customer_id", UNSET)
        customer_id: UUID | Unset
        if isinstance(_customer_id, Unset):
            customer_id = UNSET
        else:
            customer_id = UUID(_customer_id)

        def _parse_subscription_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                subscription_id_type_0 = UUID(data)

                return subscription_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        subscription_id = _parse_subscription_id(d.pop("subscription_id", UNSET))

        gateway = d.pop("gateway", UNSET)

        method = d.pop("method", UNSET)

        gateway_payment_intent_id = d.pop("gateway_payment_intent_id", UNSET)

        _status = d.pop("status", UNSET)
        status: GetPaymentAttemptResponse200DataStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = GetPaymentAttemptResponse200DataStatus(_status)

        failure_code = d.pop("failure_code", UNSET)

        amount = d.pop("amount", UNSET)

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

        def _parse_settled_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                settled_at_type_0 = datetime.datetime.fromisoformat(data)

                return settled_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        settled_at = _parse_settled_at(d.pop("settled_at", UNSET))

        get_payment_attempt_response_200_data = cls(
            id=id,
            invoice_id=invoice_id,
            invoice_number=invoice_number,
            currency=currency,
            customer_id=customer_id,
            subscription_id=subscription_id,
            gateway=gateway,
            method=method,
            gateway_payment_intent_id=gateway_payment_intent_id,
            status=status,
            failure_code=failure_code,
            amount=amount,
            created_at=created_at,
            updated_at=updated_at,
            settled_at=settled_at,
        )

        get_payment_attempt_response_200_data.additional_properties = d
        return get_payment_attempt_response_200_data

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
