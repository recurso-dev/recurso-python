from enum import Enum


class UpdateCustomerBodyTaxType(str, Enum):
    BUSINESS = "business"
    CONSUMER = "consumer"

    def __str__(self) -> str:
        return str(self.value)
