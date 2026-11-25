
import math


def assess_risk(numbers):
    # Calculate an illustrative research risk category.
    # It accepts five finite, non-negative numerical values.
    # This scoring method is for demonstration only.

    if len(numbers) != 5:
        raise ValueError("Exactly 5 features are required.")

    for value in numbers:
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError("All features must be numerical values.")
        if not math.isfinite(value):
            raise ValueError("All features must be finite numbers.")

        if value < 0:
            raise ValueError("Feature values cannot be negative.")

    total = sum(numbers)

    if total < 50:
        return "RISK"

    return "LOW RISK"
