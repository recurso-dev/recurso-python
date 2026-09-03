from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetLedgerTransactionResponse200Data")


@_attrs_define
class GetLedgerTransactionResponse200Data:
    """
    Attributes:
        transaction_id (UUID | Unset):
        timestamp (datetime.datetime | Unset):
        code (int | Unset):
        debit_account_id (UUID | Unset):
        debit_account_code (int | Unset):
        debit_account_name (str | Unset):
        credit_account_id (UUID | Unset):
        credit_account_code (int | Unset):
        credit_account_name (str | Unset):
        amount (int | Unset):
        reference_id (UUID | Unset):
        description (str | Unset):
        accounting_version (int | Unset):
        entity_id (None | Unset | UUID):
        entity_name (str | Unset):
    """

    transaction_id: UUID | Unset = UNSET
    timestamp: datetime.datetime | Unset = UNSET
    code: int | Unset = UNSET
    debit_account_id: UUID | Unset = UNSET
    debit_account_code: int | Unset = UNSET
    debit_account_name: str | Unset = UNSET
    credit_account_id: UUID | Unset = UNSET
    credit_account_code: int | Unset = UNSET
    credit_account_name: str | Unset = UNSET
    amount: int | Unset = UNSET
    reference_id: UUID | Unset = UNSET
    description: str | Unset = UNSET
    accounting_version: int | Unset = UNSET
    entity_id: None | Unset | UUID = UNSET
    entity_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        transaction_id: str | Unset = UNSET
        if not isinstance(self.transaction_id, Unset):
            transaction_id = str(self.transaction_id)

        timestamp: str | Unset = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        code = self.code

        debit_account_id: str | Unset = UNSET
        if not isinstance(self.debit_account_id, Unset):
            debit_account_id = str(self.debit_account_id)

        debit_account_code = self.debit_account_code

        debit_account_name = self.debit_account_name

        credit_account_id: str | Unset = UNSET
        if not isinstance(self.credit_account_id, Unset):
            credit_account_id = str(self.credit_account_id)

        credit_account_code = self.credit_account_code

        credit_account_name = self.credit_account_name

        amount = self.amount

        reference_id: str | Unset = UNSET
        if not isinstance(self.reference_id, Unset):
            reference_id = str(self.reference_id)

        description = self.description

        accounting_version = self.accounting_version

        entity_id: None | str | Unset
        if isinstance(self.entity_id, Unset):
            entity_id = UNSET
        elif isinstance(self.entity_id, UUID):
            entity_id = str(self.entity_id)
        else:
            entity_id = self.entity_id

        entity_name = self.entity_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if transaction_id is not UNSET:
            field_dict["transaction_id"] = transaction_id
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if code is not UNSET:
            field_dict["code"] = code
        if debit_account_id is not UNSET:
            field_dict["debit_account_id"] = debit_account_id
        if debit_account_code is not UNSET:
            field_dict["debit_account_code"] = debit_account_code
        if debit_account_name is not UNSET:
            field_dict["debit_account_name"] = debit_account_name
        if credit_account_id is not UNSET:
            field_dict["credit_account_id"] = credit_account_id
        if credit_account_code is not UNSET:
            field_dict["credit_account_code"] = credit_account_code
        if credit_account_name is not UNSET:
            field_dict["credit_account_name"] = credit_account_name
        if amount is not UNSET:
            field_dict["amount"] = amount
        if reference_id is not UNSET:
            field_dict["reference_id"] = reference_id
        if description is not UNSET:
            field_dict["description"] = description
        if accounting_version is not UNSET:
            field_dict["accounting_version"] = accounting_version
        if entity_id is not UNSET:
            field_dict["entity_id"] = entity_id
        if entity_name is not UNSET:
            field_dict["entity_name"] = entity_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _transaction_id = d.pop("transaction_id", UNSET)
        transaction_id: UUID | Unset
        if isinstance(_transaction_id, Unset):
            transaction_id = UNSET
        else:
            transaction_id = UUID(_transaction_id)

        _timestamp = d.pop("timestamp", UNSET)
        timestamp: datetime.datetime | Unset
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = datetime.datetime.fromisoformat(_timestamp)

        code = d.pop("code", UNSET)

        _debit_account_id = d.pop("debit_account_id", UNSET)
        debit_account_id: UUID | Unset
        if isinstance(_debit_account_id, Unset):
            debit_account_id = UNSET
        else:
            debit_account_id = UUID(_debit_account_id)

        debit_account_code = d.pop("debit_account_code", UNSET)

        debit_account_name = d.pop("debit_account_name", UNSET)

        _credit_account_id = d.pop("credit_account_id", UNSET)
        credit_account_id: UUID | Unset
        if isinstance(_credit_account_id, Unset):
            credit_account_id = UNSET
        else:
            credit_account_id = UUID(_credit_account_id)

        credit_account_code = d.pop("credit_account_code", UNSET)

        credit_account_name = d.pop("credit_account_name", UNSET)

        amount = d.pop("amount", UNSET)

        _reference_id = d.pop("reference_id", UNSET)
        reference_id: UUID | Unset
        if isinstance(_reference_id, Unset):
            reference_id = UNSET
        else:
            reference_id = UUID(_reference_id)

        description = d.pop("description", UNSET)

        accounting_version = d.pop("accounting_version", UNSET)

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

        entity_name = d.pop("entity_name", UNSET)

        get_ledger_transaction_response_200_data = cls(
            transaction_id=transaction_id,
            timestamp=timestamp,
            code=code,
            debit_account_id=debit_account_id,
            debit_account_code=debit_account_code,
            debit_account_name=debit_account_name,
            credit_account_id=credit_account_id,
            credit_account_code=credit_account_code,
            credit_account_name=credit_account_name,
            amount=amount,
            reference_id=reference_id,
            description=description,
            accounting_version=accounting_version,
            entity_id=entity_id,
            entity_name=entity_name,
        )

        get_ledger_transaction_response_200_data.additional_properties = d
        return get_ledger_transaction_response_200_data

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
