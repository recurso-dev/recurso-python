from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_invoice_journal_entries_response_200_data_entries_item import (
        GetInvoiceJournalEntriesResponse200DataEntriesItem,
    )


T = TypeVar("T", bound="GetInvoiceJournalEntriesResponse200Data")


@_attrs_define
class GetInvoiceJournalEntriesResponse200Data:
    """
    Attributes:
        invoice_id (UUID | Unset):
        entries (list[GetInvoiceJournalEntriesResponse200DataEntriesItem] | Unset):
    """

    invoice_id: UUID | Unset = UNSET
    entries: list[GetInvoiceJournalEntriesResponse200DataEntriesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        invoice_id: str | Unset = UNSET
        if not isinstance(self.invoice_id, Unset):
            invoice_id = str(self.invoice_id)

        entries: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.entries, Unset):
            entries = []
            for entries_item_data in self.entries:
                entries_item = entries_item_data.to_dict()
                entries.append(entries_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if invoice_id is not UNSET:
            field_dict["invoice_id"] = invoice_id
        if entries is not UNSET:
            field_dict["entries"] = entries

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_invoice_journal_entries_response_200_data_entries_item import (
            GetInvoiceJournalEntriesResponse200DataEntriesItem,
        )

        d = dict(src_dict)
        _invoice_id = d.pop("invoice_id", UNSET)
        invoice_id: UUID | Unset
        if isinstance(_invoice_id, Unset):
            invoice_id = UNSET
        else:
            invoice_id = UUID(_invoice_id)

        _entries = d.pop("entries", UNSET)
        entries: list[GetInvoiceJournalEntriesResponse200DataEntriesItem] | Unset = UNSET
        if _entries is not UNSET:
            entries = []
            for entries_item_data in _entries:
                entries_item = GetInvoiceJournalEntriesResponse200DataEntriesItem.from_dict(entries_item_data)

                entries.append(entries_item)

        get_invoice_journal_entries_response_200_data = cls(
            invoice_id=invoice_id,
            entries=entries,
        )

        get_invoice_journal_entries_response_200_data.additional_properties = d
        return get_invoice_journal_entries_response_200_data

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
