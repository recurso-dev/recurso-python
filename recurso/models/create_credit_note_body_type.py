from enum import Enum


class CreateCreditNoteBodyType(str, Enum):
    ADJUSTMENT = "adjustment"
    REFUND = "refund"

    def __str__(self) -> str:
        return str(self.value)
