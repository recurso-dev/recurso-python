from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dunning_timing_rate import DunningTimingRate


T = TypeVar("T", bound="GetDunningTimingResponse200Data")


@_attrs_define
class GetDunningTimingResponse200Data:
    """
    Attributes:
        by_hour (list[DunningTimingRate] | Unset):
        by_day_of_week (list[DunningTimingRate] | Unset):
        best_hour (int | None | Unset):
        best_day (int | None | Unset):
        sample_size (int | Unset):
    """

    by_hour: list[DunningTimingRate] | Unset = UNSET
    by_day_of_week: list[DunningTimingRate] | Unset = UNSET
    best_hour: int | None | Unset = UNSET
    best_day: int | None | Unset = UNSET
    sample_size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        by_hour: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.by_hour, Unset):
            by_hour = []
            for by_hour_item_data in self.by_hour:
                by_hour_item = by_hour_item_data.to_dict()
                by_hour.append(by_hour_item)

        by_day_of_week: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.by_day_of_week, Unset):
            by_day_of_week = []
            for by_day_of_week_item_data in self.by_day_of_week:
                by_day_of_week_item = by_day_of_week_item_data.to_dict()
                by_day_of_week.append(by_day_of_week_item)

        best_hour: int | None | Unset
        if isinstance(self.best_hour, Unset):
            best_hour = UNSET
        else:
            best_hour = self.best_hour

        best_day: int | None | Unset
        if isinstance(self.best_day, Unset):
            best_day = UNSET
        else:
            best_day = self.best_day

        sample_size = self.sample_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if by_hour is not UNSET:
            field_dict["by_hour"] = by_hour
        if by_day_of_week is not UNSET:
            field_dict["by_day_of_week"] = by_day_of_week
        if best_hour is not UNSET:
            field_dict["best_hour"] = best_hour
        if best_day is not UNSET:
            field_dict["best_day"] = best_day
        if sample_size is not UNSET:
            field_dict["sample_size"] = sample_size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dunning_timing_rate import DunningTimingRate

        d = dict(src_dict)
        _by_hour = d.pop("by_hour", UNSET)
        by_hour: list[DunningTimingRate] | Unset = UNSET
        if _by_hour is not UNSET:
            by_hour = []
            for by_hour_item_data in _by_hour:
                by_hour_item = DunningTimingRate.from_dict(by_hour_item_data)

                by_hour.append(by_hour_item)

        _by_day_of_week = d.pop("by_day_of_week", UNSET)
        by_day_of_week: list[DunningTimingRate] | Unset = UNSET
        if _by_day_of_week is not UNSET:
            by_day_of_week = []
            for by_day_of_week_item_data in _by_day_of_week:
                by_day_of_week_item = DunningTimingRate.from_dict(by_day_of_week_item_data)

                by_day_of_week.append(by_day_of_week_item)

        def _parse_best_hour(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        best_hour = _parse_best_hour(d.pop("best_hour", UNSET))

        def _parse_best_day(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        best_day = _parse_best_day(d.pop("best_day", UNSET))

        sample_size = d.pop("sample_size", UNSET)

        get_dunning_timing_response_200_data = cls(
            by_hour=by_hour,
            by_day_of_week=by_day_of_week,
            best_hour=best_hour,
            best_day=best_day,
            sample_size=sample_size,
        )

        get_dunning_timing_response_200_data.additional_properties = d
        return get_dunning_timing_response_200_data

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
