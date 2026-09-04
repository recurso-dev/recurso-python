from enum import Enum


class ListPaymentAttemptsResponse200DataItemStatus(str, Enum):
    FAILED = "failed"
    INITIATED = "initiated"
    PROCESSING = "processing"
    RETURNED = "returned"
    SUCCEEDED = "succeeded"

    def __str__(self) -> str:
        return str(self.value)
