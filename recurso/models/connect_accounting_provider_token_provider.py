from enum import Enum


class ConnectAccountingProviderTokenProvider(str, Enum):
    NETSUITE = "netsuite"
    TALLY = "tally"

    def __str__(self) -> str:
        return str(self.value)
