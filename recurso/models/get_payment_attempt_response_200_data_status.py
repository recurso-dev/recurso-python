from enum import Enum


class GetPaymentAttemptResponse200DataStatus(str, Enum):
    FAILED = "failed"
    INITIATED = "initiated"
    PROCESSING = "processing"
    RETURNED = "returned"
    SUCCEEDED = "succeeded"

    def __str__(self) -> str:
        return str(self.value)
