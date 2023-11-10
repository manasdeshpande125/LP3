class Node:
    def __init__(self, level, profit, weight, bound, items):
        self.level = level  # Level of the node in the decision tree
        self.profit = profit  # Profit at the current node
        self.weight = weight  # Weight at the current node
        self.bound = bound  # Bound of the node
        self.items = items  # List of selected items


def knapsack_branch_and_bound(profit, weight, capacity):
    n = len(profit)
    queue = []
    root = Node(-1, 0, 0, 0, [])
    queue.append(root)
    max_profit = 0
    max_items = []

    while queue:
        u = queue.pop(0)
        if u.level == n - 1:
            continue
        v = Node(u.level + 1, u.profit + profit[u.level + 1],
                 u.weight + weight[u.level + 1],
                 u.bound, u.items + [u.level + 1])
        if v.weight <= capacity and v.profit > max_profit:
            max_profit = v.profit
            max_items = v.items
        v.bound = bound(v, profit, weight, capacity, n)
        if v.bound > max_profit:
            queue.append(v)
        u.bound = bound(u, profit, weight, capacity, n)
        if u.bound > max_profit:
            queue.append(u)

    return max_profit, max_items


def bound(u, profit, weight, capacity, n):
    if u.weight >= capacity:
        return 0

    bound = u.profit
    j = u.level + 1
    total_weight = u.weight

    while j < n and total_weight + weight[j] <= capacity:
        bound += profit[j]
        total_weight += weight[j]
        j += 1

    if j < n:
        bound += (capacity - total_weight) * profit[j] / weight[j]

    return bound


profits = [10, 5, 15, 7, 6]
weights = [2, 3, 5, 7, 1]
capacity = 10

max_profit, selected_items = knapsack_branch_and_bound(
    profits, weights, capacity)
print("Maximum profit:", max_profit)
print("Selected items:", selected_items)
