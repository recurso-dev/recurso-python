from enum import Enum


class GetCollectionsQueueManagedBy(str, Enum):
    CAMPAIGN = "campaign"
    SCHEDULER = "scheduler"
    WORKER = "worker"

    def __str__(self) -> str:
        return str(self.value)
