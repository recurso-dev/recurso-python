from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime






T = TypeVar("T", bound="Entity")



@_attrs_define
class Entity:
    """ A legal entity under a tenant (Multi-Entity Books). Each entity has its own ledger and invoice series; every tenant
    has exactly one primary entity.

        Attributes:
            id (UUID | Unset):
            tenant_id (UUID | Unset):
            name (str | Unset): Display name
            legal_name (str | Unset):
            is_primary (bool | Unset): The backfill entity every tenant has; cannot be deleted.
            tb_ledger_id (int | Unset): The entity's isolated ledger id (primary is 1). Assigned automatically.
            invoice_prefix (str | Unset): Prefix for this entity's invoice series
            country_code (str | Unset): ISO 3166-1 alpha-2.
            created_at (datetime.datetime | Unset):
            updated_at (datetime.datetime | Unset):
     """

    id: UUID | Unset = UNSET
    tenant_id: UUID | Unset = UNSET
    name: str | Unset = UNSET
    legal_name: str | Unset = UNSET
    is_primary: bool | Unset = UNSET
    tb_ledger_id: int | Unset = UNSET
    invoice_prefix: str | Unset = UNSET
    country_code: str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        tenant_id: str | Unset = UNSET
        if not isinstance(self.tenant_id, Unset):
            tenant_id = str(self.tenant_id)

        name = self.name

        legal_name = self.legal_name

        is_primary = self.is_primary

        tb_ledger_id = self.tb_ledger_id

        invoice_prefix = self.invoice_prefix

        country_code = self.country_code

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if tenant_id is not UNSET:
            field_dict["tenant_id"] = tenant_id
        if name is not UNSET:
            field_dict["name"] = name
        if legal_name is not UNSET:
            field_dict["legal_name"] = legal_name
        if is_primary is not UNSET:
            field_dict["is_primary"] = is_primary
        if tb_ledger_id is not UNSET:
            field_dict["tb_ledger_id"] = tb_ledger_id
        if invoice_prefix is not UNSET:
            field_dict["invoice_prefix"] = invoice_prefix
        if country_code is not UNSET:
            field_dict["country_code"] = country_code
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        _tenant_id = d.pop("tenant_id", UNSET)
        tenant_id: UUID | Unset
        if isinstance(_tenant_id,  Unset):
            tenant_id = UNSET
        else:
            tenant_id = UUID(_tenant_id)




        name = d.pop("name", UNSET)

        legal_name = d.pop("legal_name", UNSET)

        is_primary = d.pop("is_primary", UNSET)

        tb_ledger_id = d.pop("tb_ledger_id", UNSET)

        invoice_prefix = d.pop("invoice_prefix", UNSET)

        country_code = d.pop("country_code", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at,  Unset):
            updated_at = UNSET
        else:
            updated_at = datetime.datetime.fromisoformat(_updated_at)




        entity = cls(
            id=id,
            tenant_id=tenant_id,
            name=name,
            legal_name=legal_name,
            is_primary=is_primary,
            tb_ledger_id=tb_ledger_id,
            invoice_prefix=invoice_prefix,
            country_code=country_code,
            created_at=created_at,
            updated_at=updated_at,
        )


        entity.additional_properties = d
        return entity

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
