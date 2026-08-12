from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_integration_connection_body_category import CreateIntegrationConnectionBodyCategory

if TYPE_CHECKING:
    from ..models.create_integration_connection_body_config import CreateIntegrationConnectionBodyConfig


T = TypeVar("T", bound="CreateIntegrationConnectionBody")


@_attrs_define
class CreateIntegrationConnectionBody:
    """
    Attributes:
        category (CreateIntegrationConnectionBodyCategory):
        provider (str): taxjar / avalara / ziptax / hubspot / s3.
        config (CreateIntegrationConnectionBodyConfig): Provider config (e.g. api_key; or bucket/region/keys for s3).
    """

    category: CreateIntegrationConnectionBodyCategory
    provider: str
    config: CreateIntegrationConnectionBodyConfig
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category = self.category.value

        provider = self.provider

        config = self.config.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "category": category,
                "provider": provider,
                "config": config,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_integration_connection_body_config import CreateIntegrationConnectionBodyConfig

        d = dict(src_dict)
        category = CreateIntegrationConnectionBodyCategory(d.pop("category"))

        provider = d.pop("provider")

        config = CreateIntegrationConnectionBodyConfig.from_dict(d.pop("config"))

        create_integration_connection_body = cls(
            category=category,
            provider=provider,
            config=config,
        )

        create_integration_connection_body.additional_properties = d
        return create_integration_connection_body

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
