from enum import Enum


class WalletTransactionSource(str, Enum):
    AUTO_RECHARGE = "auto_recharge"
    MANUAL = "manual"
    PROMOTIONAL = "promotional"
    VALUE_3 = ""

    def __str__(self) -> str:
        return str(self.value)
