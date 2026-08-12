from enum import Enum


class SetGatewayWebhookSecretProvider(str, Enum):
    RAZORPAY = "razorpay"
    STRIPE = "stripe"

    def __str__(self) -> str:
        return str(self.value)
