from enum import Enum


class GetTaxRegistrationsResponse200DataItemStatus(str, Enum):
    NOT_REGISTERED = "not_registered"
    PENDING = "pending"
    REGISTERED = "registered"

    def __str__(self) -> str:
        return str(self.value)
