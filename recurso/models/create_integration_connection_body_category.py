from enum import Enum


class CreateIntegrationConnectionBodyCategory(str, Enum):
    CRM = "crm"
    STORAGE = "storage"
    TAX = "tax"

    def __str__(self) -> str:
        return str(self.value)
