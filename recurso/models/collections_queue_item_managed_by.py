from enum import Enum

class CollectionsQueueItemManagedBy(str, Enum):
    CAMPAIGN = "campaign"
    SCHEDULER = "scheduler"
    WORKER = "worker"

    def __str__(self) -> str:
        return str(self.value)
