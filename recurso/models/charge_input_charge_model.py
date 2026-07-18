from enum import Enum


class ChargeInputChargeModel(str, Enum):
    GRADUATED = "graduated"
    PACKAGE = "package"
    PER_UNIT = "per_unit"
    VOLUME = "volume"

    def __str__(self) -> str:
        return str(self.value)
