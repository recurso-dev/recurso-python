from enum import Enum


class PreviewStripeImportResponse200ItemsItemKind(str, Enum):
    CUSTOMER = "customer"
    PAYMENT_METHOD = "payment_method"
    PLAN = "plan"
    SUBSCRIPTION = "subscription"

    def __str__(self) -> str:
        return str(self.value)
