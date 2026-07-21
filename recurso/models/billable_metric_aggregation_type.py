from enum import Enum


class BillableMetricAggregationType(str, Enum):
    COUNT = "count"
    CUSTOM = "custom"
    LATEST = "latest"
    MAX = "max"
    PERCENTILE = "percentile"
    SUM = "sum"
    UNIQUE = "unique"
    WEIGHTED_SUM = "weighted_sum"

    def __str__(self) -> str:
        return str(self.value)
