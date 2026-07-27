from enum import Enum


class TopUpWalletBodySource(str, Enum):
    MANUAL = "manual"
    PROMOTIONAL = "promotional"

    def __str__(self) -> str:
        return str(self.value)
