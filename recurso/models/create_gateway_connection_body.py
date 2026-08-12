from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_gateway_connection_body_mode import CreateGatewayConnectionBodyMode
from ..models.create_gateway_connection_body_provider import CreateGatewayConnectionBodyProvider
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateGatewayConnectionBody")


@_attrs_define
class CreateGatewayConnectionBody:
    """
    Attributes:
        provider (CreateGatewayConnectionBodyProvider):
        secret_key (str):
        mode (CreateGatewayConnectionBodyMode | Unset):
        public_key (str | Unset): Razorpay key_id / Stripe publishable key (not secret).
        webhook_secret (str | Unset): Optional; can be set later once the webhook URL is known.
    """

    provider: CreateGatewayConnectionBodyProvider
    secret_key: str
    mode: CreateGatewayConnectionBodyMode | Unset = UNSET
    public_key: str | Unset = UNSET
    webhook_secret: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider = self.provider.value

        secret_key = self.secret_key

        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        public_key = self.public_key

        webhook_secret = self.webhook_secret

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider": provider,
                "secret_key": secret_key,
            }
        )
        if mode is not UNSET:
            field_dict["mode"] = mode
        if public_key is not UNSET:
            field_dict["public_key"] = public_key
        if webhook_secret is not UNSET:
            field_dict["webhook_secret"] = webhook_secret

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        provider = CreateGatewayConnectionBodyProvider(d.pop("provider"))

        secret_key = d.pop("secret_key")

        _mode = d.pop("mode", UNSET)
        mode: CreateGatewayConnectionBodyMode | Unset
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = CreateGatewayConnectionBodyMode(_mode)

        public_key = d.pop("public_key", UNSET)

        webhook_secret = d.pop("webhook_secret", UNSET)

        create_gateway_connection_body = cls(
            provider=provider,
            secret_key=secret_key,
            mode=mode,
            public_key=public_key,
            webhook_secret=webhook_secret,
        )

        create_gateway_connection_body.additional_properties = d
        return create_gateway_connection_body

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
