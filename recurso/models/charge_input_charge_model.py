from enum import Enum


class ChargeInputChargeModel(str, Enum):
    DYNAMIC = "dynamic"
    GRADUATED = "graduated"
    GRADUATED_PERCENTAGE = "graduated_percentage"
    PACKAGE = "package"
    PERCENTAGE = "percentage"
    PER_UNIT = "per_unit"
    VOLUME = "volume"

    def __str__(self) -> str:
        return str(self.value)
