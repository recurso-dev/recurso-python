from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.collections_bucket import CollectionsBucket


T = TypeVar("T", bound="CollectionsFunnel")


@_attrs_define
class CollectionsFunnel:
    """The failed → resolved journey of billed revenue.

    Attributes:
        reporting_currency (str | Unset):
        past_due (CollectionsBucket | Unset): One stage of the recovery funnel, in the reporting currency.
        uncollectible (CollectionsBucket | Unset): One stage of the recovery funnel, in the reporting currency.
        recovered (CollectionsBucket | Unset): One stage of the recovery funnel, in the reporting currency.
        recovery_rate (float | Unset): Windowed concluded cohort — of cases concluded (recovered or written off) in the
            trailing rate_window_days, the fraction recovered.
        rate_window_days (int | Unset): Trailing window (days) the recovery_rate is computed over.
        fx_excluded_currencies (list[str] | Unset): Currencies whose amounts could not be converted into the reporting
            currency and are excluded from the bucket amounts (their invoices still count). Non-empty means the money
            figures are understated.
    """

    reporting_currency: str | Unset = UNSET
    past_due: CollectionsBucket | Unset = UNSET
    uncollectible: CollectionsBucket | Unset = UNSET
    recovered: CollectionsBucket | Unset = UNSET
    recovery_rate: float | Unset = UNSET
    rate_window_days: int | Unset = UNSET
    fx_excluded_currencies: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reporting_currency = self.reporting_currency

        past_due: dict[str, Any] | Unset = UNSET
        if not isinstance(self.past_due, Unset):
            past_due = self.past_due.to_dict()

        uncollectible: dict[str, Any] | Unset = UNSET
        if not isinstance(self.uncollectible, Unset):
            uncollectible = self.uncollectible.to_dict()

        recovered: dict[str, Any] | Unset = UNSET
        if not isinstance(self.recovered, Unset):
            recovered = self.recovered.to_dict()

        recovery_rate = self.recovery_rate

        rate_window_days = self.rate_window_days

        fx_excluded_currencies: list[str] | Unset = UNSET
        if not isinstance(self.fx_excluded_currencies, Unset):
            fx_excluded_currencies = self.fx_excluded_currencies

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reporting_currency is not UNSET:
            field_dict["reporting_currency"] = reporting_currency
        if past_due is not UNSET:
            field_dict["past_due"] = past_due
        if uncollectible is not UNSET:
            field_dict["uncollectible"] = uncollectible
        if recovered is not UNSET:
            field_dict["recovered"] = recovered
        if recovery_rate is not UNSET:
            field_dict["recovery_rate"] = recovery_rate
        if rate_window_days is not UNSET:
            field_dict["rate_window_days"] = rate_window_days
        if fx_excluded_currencies is not UNSET:
            field_dict["fx_excluded_currencies"] = fx_excluded_currencies

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.collections_bucket import CollectionsBucket

        d = dict(src_dict)
        reporting_currency = d.pop("reporting_currency", UNSET)

        _past_due = d.pop("past_due", UNSET)
        past_due: CollectionsBucket | Unset
        if isinstance(_past_due, Unset):
            past_due = UNSET
        else:
            past_due = CollectionsBucket.from_dict(_past_due)

        _uncollectible = d.pop("uncollectible", UNSET)
        uncollectible: CollectionsBucket | Unset
        if isinstance(_uncollectible, Unset):
            uncollectible = UNSET
        else:
            uncollectible = CollectionsBucket.from_dict(_uncollectible)

        _recovered = d.pop("recovered", UNSET)
        recovered: CollectionsBucket | Unset
        if isinstance(_recovered, Unset):
            recovered = UNSET
        else:
            recovered = CollectionsBucket.from_dict(_recovered)

        recovery_rate = d.pop("recovery_rate", UNSET)

        rate_window_days = d.pop("rate_window_days", UNSET)

        fx_excluded_currencies = cast(list[str], d.pop("fx_excluded_currencies", UNSET))

        collections_funnel = cls(
            reporting_currency=reporting_currency,
            past_due=past_due,
            uncollectible=uncollectible,
            recovered=recovered,
            recovery_rate=recovery_rate,
            rate_window_days=rate_window_days,
            fx_excluded_currencies=fx_excluded_currencies,
        )

        collections_funnel.additional_properties = d
        return collections_funnel

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
