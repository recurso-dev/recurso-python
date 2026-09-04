from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListPaymentAttemptsResponse200Pagination")


@_attrs_define
class ListPaymentAttemptsResponse200Pagination:
    """
    Attributes:
        page (int | Unset):
        per_page (int | Unset):
        total (int | Unset):
        total_pages (int | Unset):
    """

    page: int | Unset = UNSET
    per_page: int | Unset = UNSET
    total: int | Unset = UNSET
    total_pages: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        page = self.page

        per_page = self.per_page

        total = self.total

        total_pages = self.total_pages

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if page is not UNSET:
            field_dict["page"] = page
        if per_page is not UNSET:
            field_dict["per_page"] = per_page
        if total is not UNSET:
            field_dict["total"] = total
        if total_pages is not UNSET:
            field_dict["total_pages"] = total_pages

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        page = d.pop("page", UNSET)

        per_page = d.pop("per_page", UNSET)

        total = d.pop("total", UNSET)

        total_pages = d.pop("total_pages", UNSET)

        list_payment_attempts_response_200_pagination = cls(
            page=page,
            per_page=per_page,
            total=total,
            total_pages=total_pages,
        )

        list_payment_attempts_response_200_pagination.additional_properties = d
        return list_payment_attempts_response_200_pagination

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
