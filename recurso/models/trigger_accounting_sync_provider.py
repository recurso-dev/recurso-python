from enum import Enum


class TriggerAccountingSyncProvider(str, Enum):
    NETSUITE = "netsuite"
    QUICKBOOKS = "quickbooks"
    TALLY = "tally"
    XERO = "xero"

    def __str__(self) -> str:
        return str(self.value)
