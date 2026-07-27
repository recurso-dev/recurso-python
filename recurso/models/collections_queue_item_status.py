from enum import Enum

class CollectionsQueueItemStatus(str, Enum):
    PAST_DUE = "past_due"
    UNCOLLECTIBLE = "uncollectible"

    def __str__(self) -> str:
        return str(self.value)
