from enum import Enum

class InvoiceTaxRegime(str, Enum):
    GST = "gst"
    PLAIN = "plain"
    SALES_TAX = "sales_tax"
    VAT = "vat"

    def __str__(self) -> str:
        return str(self.value)
