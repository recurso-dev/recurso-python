from enum import Enum


class GetInvoicePaymentAttemptsResponse200DataAttemptsItemStatus(str, Enum):
    FAILED = "failed"
    INITIATED = "initiated"
    PROCESSING = "processing"
    RETURNED = "returned"
    SUCCEEDED = "succeeded"

    def __str__(self) -> str:
        return str(self.value)
