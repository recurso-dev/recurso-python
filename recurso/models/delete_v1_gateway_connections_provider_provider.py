from enum import Enum

class DeleteV1GatewayConnectionsProviderProvider(str, Enum):
    RAZORPAY = "razorpay"
    STRIPE = "stripe"

    def __str__(self) -> str:
        return str(self.value)
