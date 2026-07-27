from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.mrr_entity_breakdown import MRREntityBreakdown





T = TypeVar("T", bound="GetMRRByEntityResponse200Data")



@_attrs_define
class GetMRRByEntityResponse200Data:
    """ 
        Attributes:
            reporting_currency (str | Unset):
            total_mrr (int | Unset):
            entities (list[MRREntityBreakdown] | Unset):
     """

    reporting_currency: str | Unset = UNSET
    total_mrr: int | Unset = UNSET
    entities: list[MRREntityBreakdown] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.mrr_entity_breakdown import MRREntityBreakdown
        reporting_currency = self.reporting_currency

        total_mrr = self.total_mrr

        entities: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.entities, Unset):
            entities = []
            for entities_item_data in self.entities:
                entities_item = entities_item_data.to_dict()
                entities.append(entities_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if reporting_currency is not UNSET:
            field_dict["reporting_currency"] = reporting_currency
        if total_mrr is not UNSET:
            field_dict["total_mrr"] = total_mrr
        if entities is not UNSET:
            field_dict["entities"] = entities

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mrr_entity_breakdown import MRREntityBreakdown
        d = dict(src_dict)
        reporting_currency = d.pop("reporting_currency", UNSET)

        total_mrr = d.pop("total_mrr", UNSET)

        _entities = d.pop("entities", UNSET)
        entities: list[MRREntityBreakdown] | Unset = UNSET
        if _entities is not UNSET:
            entities = []
            for entities_item_data in _entities:
                entities_item = MRREntityBreakdown.from_dict(entities_item_data)



                entities.append(entities_item)


        get_mrr_by_entity_response_200_data = cls(
            reporting_currency=reporting_currency,
            total_mrr=total_mrr,
            entities=entities,
        )


        get_mrr_by_entity_response_200_data.additional_properties = d
        return get_mrr_by_entity_response_200_data

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
