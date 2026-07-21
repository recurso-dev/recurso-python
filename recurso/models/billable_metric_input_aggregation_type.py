from enum import Enum


class BillableMetricInputAggregationType(str, Enum):
    COUNT = "count"
    LATEST = "latest"
    MAX = "max"
    PERCENTILE = "percentile"
    SUM = "sum"
    UNIQUE = "unique"

    def __str__(self) -> str:
        return str(self.value)
