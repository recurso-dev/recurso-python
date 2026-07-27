from enum import Enum


class GatewayConnectionViewProvider(str, Enum):
    GOCARDLESS = "gocardless"
    RAZORPAY = "razorpay"
    STRIPE = "stripe"

    def __str__(self) -> str:
        return str(self.value)
