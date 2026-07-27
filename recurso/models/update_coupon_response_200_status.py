from enum import Enum


class UpdateCouponResponse200Status(str, Enum):
    ACTIVATED = "activated"
    DEACTIVATED = "deactivated"

    def __str__(self) -> str:
        return str(self.value)
