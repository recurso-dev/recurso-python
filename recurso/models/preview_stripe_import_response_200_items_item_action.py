from enum import Enum


class PreviewStripeImportResponse200ItemsItemAction(str, Enum):
    CONFLICT = "conflict"
    CREATE = "create"
    LINK_EXISTING = "link_existing"
    SKIP_ALREADY_IMPORTED = "skip_already_imported"
    UNSUPPORTED = "unsupported"

    def __str__(self) -> str:
        return str(self.value)
