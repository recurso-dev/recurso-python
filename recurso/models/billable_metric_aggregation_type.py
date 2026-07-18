from enum import Enum


class BillableMetricAggregationType(str, Enum):
    COUNT = "count"
    MAX = "max"
    SUM = "sum"
    UNIQUE = "unique"

    def __str__(self) -> str:
        return str(self.value)
