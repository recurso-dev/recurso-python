from enum import Enum


class DeleteGatewayConnectionProvider(str, Enum):
    RAZORPAY = "razorpay"
    STRIPE = "stripe"

    def __str__(self) -> str:
        return str(self.value)
