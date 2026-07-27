from enum import Enum

class GetCollectionsQueueStatus(str, Enum):
    PAST_DUE = "past_due"
    UNCOLLECTIBLE = "uncollectible"

    def __str__(self) -> str:
        return str(self.value)
