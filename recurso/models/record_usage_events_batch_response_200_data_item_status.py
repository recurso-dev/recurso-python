from enum import Enum


class RecordUsageEventsBatchResponse200DataItemStatus(str, Enum):
    DUPLICATE = "duplicate"
    ERROR = "error"
    RECORDED = "recorded"

    def __str__(self) -> str:
        return str(self.value)
