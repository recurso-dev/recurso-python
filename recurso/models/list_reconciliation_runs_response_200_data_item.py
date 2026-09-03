from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListReconciliationRunsResponse200DataItem")


@_attrs_define
class ListReconciliationRunsResponse200DataItem:
    """
    Attributes:
        id (UUID | Unset):
        run_by (None | Unset | UUID):
        run_at (datetime.datetime | Unset):
        invoices_checked (int | Unset):
        paid_invoices_checked (int | Unset):
        total_discrepancies (int | Unset):
        tb_compared (bool | Unset):
        tb_accounts_checked (int | Unset):
        tb_transfers_checked (int | Unset):
        created_at (datetime.datetime | Unset):
    """

    id: UUID | Unset = UNSET
    run_by: None | Unset | UUID = UNSET
    run_at: datetime.datetime | Unset = UNSET
    invoices_checked: int | Unset = UNSET
    paid_invoices_checked: int | Unset = UNSET
    total_discrepancies: int | Unset = UNSET
    tb_compared: bool | Unset = UNSET
    tb_accounts_checked: int | Unset = UNSET
    tb_transfers_checked: int | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        run_by: None | str | Unset
        if isinstance(self.run_by, Unset):
            run_by = UNSET
        elif isinstance(self.run_by, UUID):
            run_by = str(self.run_by)
        else:
            run_by = self.run_by

        run_at: str | Unset = UNSET
        if not isinstance(self.run_at, Unset):
            run_at = self.run_at.isoformat()

        invoices_checked = self.invoices_checked

        paid_invoices_checked = self.paid_invoices_checked

        total_discrepancies = self.total_discrepancies

        tb_compared = self.tb_compared

        tb_accounts_checked = self.tb_accounts_checked

        tb_transfers_checked = self.tb_transfers_checked

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if run_by is not UNSET:
            field_dict["run_by"] = run_by
        if run_at is not UNSET:
            field_dict["run_at"] = run_at
        if invoices_checked is not UNSET:
            field_dict["invoices_checked"] = invoices_checked
        if paid_invoices_checked is not UNSET:
            field_dict["paid_invoices_checked"] = paid_invoices_checked
        if total_discrepancies is not UNSET:
            field_dict["total_discrepancies"] = total_discrepancies
        if tb_compared is not UNSET:
            field_dict["tb_compared"] = tb_compared
        if tb_accounts_checked is not UNSET:
            field_dict["tb_accounts_checked"] = tb_accounts_checked
        if tb_transfers_checked is not UNSET:
            field_dict["tb_transfers_checked"] = tb_transfers_checked
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

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

        def _parse_run_by(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                run_by_type_0 = UUID(data)

                return run_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        run_by = _parse_run_by(d.pop("run_by", UNSET))

        _run_at = d.pop("run_at", UNSET)
        run_at: datetime.datetime | Unset
        if isinstance(_run_at, Unset):
            run_at = UNSET
        else:
            run_at = datetime.datetime.fromisoformat(_run_at)

        invoices_checked = d.pop("invoices_checked", UNSET)

        paid_invoices_checked = d.pop("paid_invoices_checked", UNSET)

        total_discrepancies = d.pop("total_discrepancies", UNSET)

        tb_compared = d.pop("tb_compared", UNSET)

        tb_accounts_checked = d.pop("tb_accounts_checked", UNSET)

        tb_transfers_checked = d.pop("tb_transfers_checked", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        list_reconciliation_runs_response_200_data_item = cls(
            id=id,
            run_by=run_by,
            run_at=run_at,
            invoices_checked=invoices_checked,
            paid_invoices_checked=paid_invoices_checked,
            total_discrepancies=total_discrepancies,
            tb_compared=tb_compared,
            tb_accounts_checked=tb_accounts_checked,
            tb_transfers_checked=tb_transfers_checked,
            created_at=created_at,
        )

        list_reconciliation_runs_response_200_data_item.additional_properties = d
        return list_reconciliation_runs_response_200_data_item

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
