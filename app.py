def assess_risk(numbers):
    if len(numbers) != 5:
        raise ValueError("Enter all 5 features.")

    total = sum(numbers)

    if total < 50:
        return "RISK"

    return "LOW RISK"