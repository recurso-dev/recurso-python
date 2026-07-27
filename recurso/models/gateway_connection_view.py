from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.gateway_connection_view_mode import GatewayConnectionViewMode
from ..models.gateway_connection_view_provider import GatewayConnectionViewProvider
from ..types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime






T = TypeVar("T", bound="GatewayConnectionView")



@_attrs_define
class GatewayConnectionView:
    """ Secret-free projection of a BYO gateway connection.

        Attributes:
            id (UUID | Unset):
            provider (GatewayConnectionViewProvider | Unset):
            mode (GatewayConnectionViewMode | Unset):
            public_key (str | Unset):
            has_webhook_secret (bool | Unset):
            webhook_path (str | Unset): Append to the API origin for the gateway console (e.g. /webhooks/stripe/{id}).
            created_at (datetime.datetime | Unset):
            updated_at (datetime.datetime | Unset):
     """

    id: UUID | Unset = UNSET
    provider: GatewayConnectionViewProvider | Unset = UNSET
    mode: GatewayConnectionViewMode | Unset = UNSET
    public_key: str | Unset = UNSET
    has_webhook_secret: bool | Unset = UNSET
    webhook_path: str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        provider: str | Unset = UNSET
        if not isinstance(self.provider, Unset):
            provider = self.provider.value


        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value


        public_key = self.public_key

        has_webhook_secret = self.has_webhook_secret

        webhook_path = self.webhook_path

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
        if provider is not UNSET:
            field_dict["provider"] = provider
        if mode is not UNSET:
            field_dict["mode"] = mode
        if public_key is not UNSET:
            field_dict["public_key"] = public_key
        if has_webhook_secret is not UNSET:
            field_dict["has_webhook_secret"] = has_webhook_secret
        if webhook_path is not UNSET:
            field_dict["webhook_path"] = webhook_path
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




        _provider = d.pop("provider", UNSET)
        provider: GatewayConnectionViewProvider | Unset
        if isinstance(_provider,  Unset):
            provider = UNSET
        else:
            provider = GatewayConnectionViewProvider(_provider)




        _mode = d.pop("mode", UNSET)
        mode: GatewayConnectionViewMode | Unset
        if isinstance(_mode,  Unset):
            mode = UNSET
        else:
            mode = GatewayConnectionViewMode(_mode)




        public_key = d.pop("public_key", UNSET)

        has_webhook_secret = d.pop("has_webhook_secret", UNSET)

        webhook_path = d.pop("webhook_path", UNSET)

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




        gateway_connection_view = cls(
            id=id,
            provider=provider,
            mode=mode,
            public_key=public_key,
            has_webhook_secret=has_webhook_secret,
            webhook_path=webhook_path,
            created_at=created_at,
            updated_at=updated_at,
        )


        gateway_connection_view.additional_properties = d
        return gateway_connection_view

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
