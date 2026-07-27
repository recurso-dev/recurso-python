from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_mandate_body_frequency import CreateMandateBodyFrequency
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateMandateBody")


@_attrs_define
class CreateMandateBody:
    """
    Attributes:
        customer_id (UUID):
        max_amount (int): Maximum per-debit amount in the lowest currency unit.
        frequency (CreateMandateBodyFrequency):
        currency (str | Unset): Mandate rail. Empty/INR = Razorpay UPI AutoPay; an overridden currency (e.g. EUR) = bank
            debit via GoCardless. VPA is only required for INR.
        subscription_id (UUID | Unset):
        vpa (str | Unset): Customer UPI VPA (e.g. `name@bank`).
    """

    customer_id: UUID
    max_amount: int
    frequency: CreateMandateBodyFrequency
    currency: str | Unset = UNSET
    subscription_id: UUID | Unset = UNSET
    vpa: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        customer_id = str(self.customer_id)

        max_amount = self.max_amount

        frequency = self.frequency.value

        currency = self.currency

        subscription_id: str | Unset = UNSET
        if not isinstance(self.subscription_id, Unset):
            subscription_id = str(self.subscription_id)

        vpa = self.vpa

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "customer_id": customer_id,
                "max_amount": max_amount,
                "frequency": frequency,
            }
        )
        if currency is not UNSET:
            field_dict["currency"] = currency
        if subscription_id is not UNSET:
            field_dict["subscription_id"] = subscription_id
        if vpa is not UNSET:
            field_dict["vpa"] = vpa

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        customer_id = UUID(d.pop("customer_id"))

        max_amount = d.pop("max_amount")

        frequency = CreateMandateBodyFrequency(d.pop("frequency"))

        currency = d.pop("currency", UNSET)

        _subscription_id = d.pop("subscription_id", UNSET)
        subscription_id: UUID | Unset
        if isinstance(_subscription_id, Unset):
            subscription_id = UNSET
        else:
            subscription_id = UUID(_subscription_id)

        vpa = d.pop("vpa", UNSET)

        create_mandate_body = cls(
            customer_id=customer_id,
            max_amount=max_amount,
            frequency=frequency,
            currency=currency,
            subscription_id=subscription_id,
            vpa=vpa,
        )

        create_mandate_body.additional_properties = d
        return create_mandate_body

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
