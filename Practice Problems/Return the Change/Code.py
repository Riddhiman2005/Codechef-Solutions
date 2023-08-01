def calculate_returned_amount(cost):
    rounded_cost = (cost + 5) // 10 * 10  # Round the cost to the nearest multiple of 10
    return max(0, 100 - rounded_cost)  # Calculate the amount returned

# Input
T = int(input())

for _ in range(T):
    X = int(input())
    amount_returned = calculate_returned_amount(X)
    print(amount_returned)
