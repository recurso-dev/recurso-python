from enum import Enum

class PostV1GatewayConnectionsBodyProvider(str, Enum):
    RAZORPAY = "razorpay"
    STRIPE = "stripe"

    def __str__(self) -> str:
        return str(self.value)
