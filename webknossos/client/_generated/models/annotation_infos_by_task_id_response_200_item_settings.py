from typing import Any, Dict, List, Type, TypeVar, cast

import attr

from ..models.annotation_infos_by_task_id_response_200_item_settings_resolution_restrictions import (
    AnnotationInfosByTaskIdResponse200ItemSettingsResolutionRestrictions,
)

T = TypeVar("T", bound="AnnotationInfosByTaskIdResponse200ItemSettings")


@attr.s(auto_attribs=True)
class AnnotationInfosByTaskIdResponse200ItemSettings:
    """ """

    allowed_modes: List[str]
    branch_points_allowed: int
    soma_clicking_allowed: int
    merger_mode: int
    resolution_restrictions: AnnotationInfosByTaskIdResponse200ItemSettingsResolutionRestrictions
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        allowed_modes = self.allowed_modes

        branch_points_allowed = self.branch_points_allowed
        soma_clicking_allowed = self.soma_clicking_allowed
        merger_mode = self.merger_mode
        resolution_restrictions = self.resolution_restrictions.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "allowedModes": allowed_modes,
                "branchPointsAllowed": branch_points_allowed,
                "somaClickingAllowed": soma_clicking_allowed,
                "mergerMode": merger_mode,
                "resolutionRestrictions": resolution_restrictions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        allowed_modes = cast(List[str], d.pop("allowedModes"))

        branch_points_allowed = d.pop("branchPointsAllowed")

        soma_clicking_allowed = d.pop("somaClickingAllowed")

        merger_mode = d.pop("mergerMode")

        resolution_restrictions = AnnotationInfosByTaskIdResponse200ItemSettingsResolutionRestrictions.from_dict(
            d.pop("resolutionRestrictions")
        )

        annotation_infos_by_task_id_response_200_item_settings = cls(
            allowed_modes=allowed_modes,
            branch_points_allowed=branch_points_allowed,
            soma_clicking_allowed=soma_clicking_allowed,
            merger_mode=merger_mode,
            resolution_restrictions=resolution_restrictions,
        )

        annotation_infos_by_task_id_response_200_item_settings.additional_properties = d
        return annotation_infos_by_task_id_response_200_item_settings

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
