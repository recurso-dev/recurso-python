from enum import Enum


class PreviewChargebeeImportResponse200ItemsItemKind(str, Enum):
    CUSTOMER = "customer"
    PLAN = "plan"
    SUBSCRIPTION = "subscription"

    def __str__(self) -> str:
        return str(self.value)
