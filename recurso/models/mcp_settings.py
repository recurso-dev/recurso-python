from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MCPSettings")


@_attrs_define
class MCPSettings:
    """A tenant's MCP server opt-in.

    Attributes:
        tier3_enabled (bool | Unset): When true, AI agents may run money-path / destructive MCP tools (convert quote to
            invoice, cancel subscription, issue credit note, top up wallet, …) against this tenant. Off by default.
    """

    tier3_enabled: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tier3_enabled = self.tier3_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tier3_enabled is not UNSET:
            field_dict["tier3_enabled"] = tier3_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tier3_enabled = d.pop("tier3_enabled", UNSET)

        mcp_settings = cls(
            tier3_enabled=tier3_enabled,
        )

        mcp_settings.additional_properties = d
        return mcp_settings

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
