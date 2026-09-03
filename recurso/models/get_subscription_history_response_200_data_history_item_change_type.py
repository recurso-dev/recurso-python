from enum import Enum


class GetSubscriptionHistoryResponse200DataHistoryItemChangeType(str, Enum):
    PLAN = "plan"
    STATUS = "status"

    def __str__(self) -> str:
        return str(self.value)
