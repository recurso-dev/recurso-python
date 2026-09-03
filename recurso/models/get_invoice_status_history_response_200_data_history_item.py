from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetInvoiceStatusHistoryResponse200DataHistoryItem")


@_attrs_define
class GetInvoiceStatusHistoryResponse200DataHistoryItem:
    """
    Attributes:
        id (UUID | Unset):
        invoice_id (UUID | Unset):
        from_status (None | str | Unset):
        to_status (str | Unset):
        changed_at (datetime.datetime | Unset):
    """

    id: UUID | Unset = UNSET
    invoice_id: UUID | Unset = UNSET
    from_status: None | str | Unset = UNSET
    to_status: str | Unset = UNSET
    changed_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        invoice_id: str | Unset = UNSET
        if not isinstance(self.invoice_id, Unset):
            invoice_id = str(self.invoice_id)

        from_status: None | str | Unset
        if isinstance(self.from_status, Unset):
            from_status = UNSET
        else:
            from_status = self.from_status

        to_status = self.to_status

        changed_at: str | Unset = UNSET
        if not isinstance(self.changed_at, Unset):
            changed_at = self.changed_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if invoice_id is not UNSET:
            field_dict["invoice_id"] = invoice_id
        if from_status is not UNSET:
            field_dict["from_status"] = from_status
        if to_status is not UNSET:
            field_dict["to_status"] = to_status
        if changed_at is not UNSET:
            field_dict["changed_at"] = changed_at

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

        def _parse_from_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        from_status = _parse_from_status(d.pop("from_status", UNSET))

        to_status = d.pop("to_status", UNSET)

        _changed_at = d.pop("changed_at", UNSET)
        changed_at: datetime.datetime | Unset
        if isinstance(_changed_at, Unset):
            changed_at = UNSET
        else:
            changed_at = datetime.datetime.fromisoformat(_changed_at)

        get_invoice_status_history_response_200_data_history_item = cls(
            id=id,
            invoice_id=invoice_id,
            from_status=from_status,
            to_status=to_status,
            changed_at=changed_at,
        )

        get_invoice_status_history_response_200_data_history_item.additional_properties = d
        return get_invoice_status_history_response_200_data_history_item

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
