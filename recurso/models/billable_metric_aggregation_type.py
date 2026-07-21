from enum import Enum


class BillableMetricAggregationType(str, Enum):
    COUNT = "count"
    LATEST = "latest"
    MAX = "max"
    PERCENTILE = "percentile"
    SUM = "sum"
    UNIQUE = "unique"

    def __str__(self) -> str:
        return str(self.value)
