from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuditLog")


@_attrs_define
class AuditLog:
    """One immutable record of a config-grade mutation.

    Attributes:
        id (UUID | Unset):
        actor (str | Unset): Dashboard user id, or api_key
        action (str | Unset): METHOD + route template
        entity_type (str | Unset):
        entity_id (str | Unset):
        status (int | Unset):
        request_body (str | Unset): Truncated to 4KB
        ip (str | Unset):
        created_at (datetime.datetime | Unset):
    """

    id: UUID | Unset = UNSET
    actor: str | Unset = UNSET
    action: str | Unset = UNSET
    entity_type: str | Unset = UNSET
    entity_id: str | Unset = UNSET
    status: int | Unset = UNSET
    request_body: str | Unset = UNSET
    ip: str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        actor = self.actor

        action = self.action

        entity_type = self.entity_type

        entity_id = self.entity_id

        status = self.status

        request_body = self.request_body

        ip = self.ip

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if actor is not UNSET:
            field_dict["actor"] = actor
        if action is not UNSET:
            field_dict["action"] = action
        if entity_type is not UNSET:
            field_dict["entity_type"] = entity_type
        if entity_id is not UNSET:
            field_dict["entity_id"] = entity_id
        if status is not UNSET:
            field_dict["status"] = status
        if request_body is not UNSET:
            field_dict["request_body"] = request_body
        if ip is not UNSET:
            field_dict["ip"] = ip
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

        actor = d.pop("actor", UNSET)

        action = d.pop("action", UNSET)

        entity_type = d.pop("entity_type", UNSET)

        entity_id = d.pop("entity_id", UNSET)

        status = d.pop("status", UNSET)

        request_body = d.pop("request_body", UNSET)

        ip = d.pop("ip", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        audit_log = cls(
            id=id,
            actor=actor,
            action=action,
            entity_type=entity_type,
            entity_id=entity_id,
            status=status,
            request_body=request_body,
            ip=ip,
            created_at=created_at,
        )

        audit_log.additional_properties = d
        return audit_log

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
