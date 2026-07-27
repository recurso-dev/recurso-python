from enum import Enum

class PutV1GatewayConnectionsProviderWebhookSecretProvider(str, Enum):
    RAZORPAY = "razorpay"
    STRIPE = "stripe"

    def __str__(self) -> str:
        return str(self.value)
