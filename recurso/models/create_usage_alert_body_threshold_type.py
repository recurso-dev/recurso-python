from enum import Enum


class CreateUsageAlertBodyThresholdType(str, Enum):
    PERCENT_OF_LIMIT = "percent_of_limit"
    QUANTITY = "quantity"

    def __str__(self) -> str:
        return str(self.value)
