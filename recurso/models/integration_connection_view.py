from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.integration_connection_view_category import IntegrationConnectionViewCategory
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.integration_connection_view_config import IntegrationConnectionViewConfig


T = TypeVar("T", bound="IntegrationConnectionView")


@_attrs_define
class IntegrationConnectionView:
    """Secret-free projection of a BYO tax/CRM/storage connection.

    Attributes:
        id (UUID | Unset):
        category (IntegrationConnectionViewCategory | Unset):
        provider (str | Unset):
        config (IntegrationConnectionViewConfig | Unset): Non-secret config fields only (e.g. region, bucket,
            endpoints).
        has_secrets (bool | Unset):
        created_at (datetime.datetime | Unset):
        updated_at (datetime.datetime | Unset):
    """

    id: UUID | Unset = UNSET
    category: IntegrationConnectionViewCategory | Unset = UNSET
    provider: str | Unset = UNSET
    config: IntegrationConnectionViewConfig | Unset = UNSET
    has_secrets: bool | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        category: str | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.value

        provider = self.provider

        config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        has_secrets = self.has_secrets

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if category is not UNSET:
            field_dict["category"] = category
        if provider is not UNSET:
            field_dict["provider"] = provider
        if config is not UNSET:
            field_dict["config"] = config
        if has_secrets is not UNSET:
            field_dict["has_secrets"] = has_secrets
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.integration_connection_view_config import IntegrationConnectionViewConfig

        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        _category = d.pop("category", UNSET)
        category: IntegrationConnectionViewCategory | Unset
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = IntegrationConnectionViewCategory(_category)

        provider = d.pop("provider", UNSET)

        _config = d.pop("config", UNSET)
        config: IntegrationConnectionViewConfig | Unset
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = IntegrationConnectionViewConfig.from_dict(_config)

        has_secrets = d.pop("has_secrets", UNSET)

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

        integration_connection_view = cls(
            id=id,
            category=category,
            provider=provider,
            config=config,
            has_secrets=has_secrets,
            created_at=created_at,
            updated_at=updated_at,
        )

        integration_connection_view.additional_properties = d
        return integration_connection_view

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
