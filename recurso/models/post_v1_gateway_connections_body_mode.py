from enum import Enum


class PostV1GatewayConnectionsBodyMode(str, Enum):
    LIVE = "live"
    TEST = "test"

    def __str__(self) -> str:
        return str(self.value)
