from dataclasses import dataclass, field
from typing import List


@dataclass
class Calculator:
    """Simple calculator that also keeps a history of performed calculations.

    history: List[str] stores human-readable records like '2.0 + 3.0 = 5.0'.
    """
    history: List[str] = field(default_factory=list)

    def add(self, a, b):
        return float(a) + float(b)

    def subtract(self, a, b):
        return float(a) - float(b)

    def multiply(self, a, b):
        return float(a) * float(b)

    def divide(self, a, b):
        if float(b) == 0.0:
            raise ValueError("Cannot divide by zero.")
        return float(a) / float(b)
