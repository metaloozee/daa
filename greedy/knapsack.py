"""
NOTE: This is the standard (fractional) knapsack problem.
"""

def knapsack(profits: list[float], weights: list[float], capacity: float) -> float:
    items = list(zip(profits, weights))
    items.sort(key=lambda item: item[0] / item[1], reverse=True)

    current_weight = 0.0
    total_value = 0.0

    for profit, weight in items:
        if current_weight + weight <= capacity:
            current_weight += weight
            total_value += profit
        else:
            fraction = (capacity - current_weight) / weight
            total_value += fraction * profit
            break

    return total_value
