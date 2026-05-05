def score_contract(value: float, days_to_expiry: int):
    score = 0
    rationale = []

    if value >= 5_000_000:
        score += 40
        rationale.append("High-value contract.")
    elif value >= 800_000:
        score += 25
        rationale.append("Mid-value contract.")
    else:
        score += 10
        rationale.append("Lower-value contract.")

    if days_to_expiry <= 60:
        score += 40
        rationale.append("Near-term expiry.")
    elif days_to_expiry <= 180:
        score += 25
        rationale.append("Mid-term expiry.")
    else:
        score += 10
        rationale.append("Distant expiry.")

    if score >= 65:
        priority = "High"
        recommendation = "Prioritize renegotiation"
    elif score >= 35:
        priority = "Medium"
        recommendation = "Monitor and prepare renegotiation"
    else:
        priority = "Low"
        recommendation = "Low priority"

    return score, priority, recommendation, rationale