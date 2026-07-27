from enum import Enum


class WalletTransactionType(str, Enum):
    DRAIN = "drain"
    EXPIRY = "expiry"
    TOP_UP = "top_up"

    def __str__(self) -> str:
        return str(self.value)
