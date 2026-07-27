from enum import Enum


class SetTaxRegistrationsBodyRegistrationsItemStatus(str, Enum):
    NOT_REGISTERED = "not_registered"
    PENDING = "pending"
    REGISTERED = "registered"

    def __str__(self) -> str:
        return str(self.value)
