from enum import Enum


class CreditNoteStatus(str, Enum):
    EXPIRED = "expired"
    ISSUED = "issued"
    PENDING_APPROVAL = "pending_approval"
    REJECTED = "rejected"
    USED = "used"
    VOID = "void"

    def __str__(self) -> str:
        return str(self.value)
