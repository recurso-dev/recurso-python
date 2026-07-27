from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.credit_note import CreditNote
    from ..models.gift import Gift


T = TypeVar("T", bound="CancelGiftResponse200Data")


@_attrs_define
class CancelGiftResponse200Data:
    """
    Attributes:
        gift (Gift | Unset):
        credit_note (CreditNote | Unset):
        invoice_voided (bool | Unset):
    """

    gift: Gift | Unset = UNSET
    credit_note: CreditNote | Unset = UNSET
    invoice_voided: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        gift: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gift, Unset):
            gift = self.gift.to_dict()

        credit_note: dict[str, Any] | Unset = UNSET
        if not isinstance(self.credit_note, Unset):
            credit_note = self.credit_note.to_dict()

        invoice_voided = self.invoice_voided

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if gift is not UNSET:
            field_dict["gift"] = gift
        if credit_note is not UNSET:
            field_dict["credit_note"] = credit_note
        if invoice_voided is not UNSET:
            field_dict["invoice_voided"] = invoice_voided

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.credit_note import CreditNote
        from ..models.gift import Gift

        d = dict(src_dict)
        _gift = d.pop("gift", UNSET)
        gift: Gift | Unset
        if isinstance(_gift, Unset):
            gift = UNSET
        else:
            gift = Gift.from_dict(_gift)

        _credit_note = d.pop("credit_note", UNSET)
        credit_note: CreditNote | Unset
        if isinstance(_credit_note, Unset):
            credit_note = UNSET
        else:
            credit_note = CreditNote.from_dict(_credit_note)

        invoice_voided = d.pop("invoice_voided", UNSET)

        cancel_gift_response_200_data = cls(
            gift=gift,
            credit_note=credit_note,
            invoice_voided=invoice_voided,
        )

        cancel_gift_response_200_data.additional_properties = d
        return cancel_gift_response_200_data

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
