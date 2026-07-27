from enum import Enum

class PostV1IntegrationConnectionsBodyCategory(str, Enum):
    CRM = "crm"
    STORAGE = "storage"
    TAX = "tax"

    def __str__(self) -> str:
        return str(self.value)
