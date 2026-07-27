from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.credit_note import CreditNote
    from ..models.get_credit_statement_response_200_data_applications_item import (
        GetCreditStatementResponse200DataApplicationsItem,
    )
    from ..models.get_credit_statement_response_200_data_balances_item import (
        GetCreditStatementResponse200DataBalancesItem,
    )
    from ..models.get_credit_statement_response_200_data_summary_item import (
        GetCreditStatementResponse200DataSummaryItem,
    )


T = TypeVar("T", bound="GetCreditStatementResponse200Data")


@_attrs_define
class GetCreditStatementResponse200Data:
    """
    Attributes:
        customer_id (UUID | Unset):
        balances (list[GetCreditStatementResponse200DataBalancesItem] | Unset):
        grants (list[CreditNote] | Unset):
        applications (list[GetCreditStatementResponse200DataApplicationsItem] | Unset):
        summary (list[GetCreditStatementResponse200DataSummaryItem] | Unset):
    """

    customer_id: UUID | Unset = UNSET
    balances: list[GetCreditStatementResponse200DataBalancesItem] | Unset = UNSET
    grants: list[CreditNote] | Unset = UNSET
    applications: list[GetCreditStatementResponse200DataApplicationsItem] | Unset = UNSET
    summary: list[GetCreditStatementResponse200DataSummaryItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        customer_id: str | Unset = UNSET
        if not isinstance(self.customer_id, Unset):
            customer_id = str(self.customer_id)

        balances: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.balances, Unset):
            balances = []
            for balances_item_data in self.balances:
                balances_item = balances_item_data.to_dict()
                balances.append(balances_item)

        grants: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.grants, Unset):
            grants = []
            for grants_item_data in self.grants:
                grants_item = grants_item_data.to_dict()
                grants.append(grants_item)

        applications: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.applications, Unset):
            applications = []
            for applications_item_data in self.applications:
                applications_item = applications_item_data.to_dict()
                applications.append(applications_item)

        summary: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.summary, Unset):
            summary = []
            for summary_item_data in self.summary:
                summary_item = summary_item_data.to_dict()
                summary.append(summary_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if customer_id is not UNSET:
            field_dict["customer_id"] = customer_id
        if balances is not UNSET:
            field_dict["balances"] = balances
        if grants is not UNSET:
            field_dict["grants"] = grants
        if applications is not UNSET:
            field_dict["applications"] = applications
        if summary is not UNSET:
            field_dict["summary"] = summary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.credit_note import CreditNote
        from ..models.get_credit_statement_response_200_data_applications_item import (
            GetCreditStatementResponse200DataApplicationsItem,
        )
        from ..models.get_credit_statement_response_200_data_balances_item import (
            GetCreditStatementResponse200DataBalancesItem,
        )
        from ..models.get_credit_statement_response_200_data_summary_item import (
            GetCreditStatementResponse200DataSummaryItem,
        )

        d = dict(src_dict)
        _customer_id = d.pop("customer_id", UNSET)
        customer_id: UUID | Unset
        if isinstance(_customer_id, Unset):
            customer_id = UNSET
        else:
            customer_id = UUID(_customer_id)

        _balances = d.pop("balances", UNSET)
        balances: list[GetCreditStatementResponse200DataBalancesItem] | Unset = UNSET
        if _balances is not UNSET:
            balances = []
            for balances_item_data in _balances:
                balances_item = GetCreditStatementResponse200DataBalancesItem.from_dict(balances_item_data)

                balances.append(balances_item)

        _grants = d.pop("grants", UNSET)
        grants: list[CreditNote] | Unset = UNSET
        if _grants is not UNSET:
            grants = []
            for grants_item_data in _grants:
                grants_item = CreditNote.from_dict(grants_item_data)

                grants.append(grants_item)

        _applications = d.pop("applications", UNSET)
        applications: list[GetCreditStatementResponse200DataApplicationsItem] | Unset = UNSET
        if _applications is not UNSET:
            applications = []
            for applications_item_data in _applications:
                applications_item = GetCreditStatementResponse200DataApplicationsItem.from_dict(applications_item_data)

                applications.append(applications_item)

        _summary = d.pop("summary", UNSET)
        summary: list[GetCreditStatementResponse200DataSummaryItem] | Unset = UNSET
        if _summary is not UNSET:
            summary = []
            for summary_item_data in _summary:
                summary_item = GetCreditStatementResponse200DataSummaryItem.from_dict(summary_item_data)

                summary.append(summary_item)

        get_credit_statement_response_200_data = cls(
            customer_id=customer_id,
            balances=balances,
            grants=grants,
            applications=applications,
            summary=summary,
        )

        get_credit_statement_response_200_data.additional_properties = d
        return get_credit_statement_response_200_data

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
