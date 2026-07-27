from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.integration_connection_view import IntegrationConnectionView





T = TypeVar("T", bound="GetV1IntegrationConnectionsResponse200Data")



@_attrs_define
class GetV1IntegrationConnectionsResponse200Data:
    """ 
        Attributes:
            connections (list[IntegrationConnectionView] | Unset):
            vault_ready (bool | Unset):
     """

    connections: list[IntegrationConnectionView] | Unset = UNSET
    vault_ready: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.integration_connection_view import IntegrationConnectionView
        connections: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.connections, Unset):
            connections = []
            for connections_item_data in self.connections:
                connections_item = connections_item_data.to_dict()
                connections.append(connections_item)



        vault_ready = self.vault_ready


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if connections is not UNSET:
            field_dict["connections"] = connections
        if vault_ready is not UNSET:
            field_dict["vault_ready"] = vault_ready

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.integration_connection_view import IntegrationConnectionView
        d = dict(src_dict)
        _connections = d.pop("connections", UNSET)
        connections: list[IntegrationConnectionView] | Unset = UNSET
        if _connections is not UNSET:
            connections = []
            for connections_item_data in _connections:
                connections_item = IntegrationConnectionView.from_dict(connections_item_data)



                connections.append(connections_item)


        vault_ready = d.pop("vault_ready", UNSET)

        get_v1_integration_connections_response_200_data = cls(
            connections=connections,
            vault_ready=vault_ready,
        )


        get_v1_integration_connections_response_200_data.additional_properties = d
        return get_v1_integration_connections_response_200_data

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
