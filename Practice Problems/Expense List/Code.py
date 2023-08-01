def calculate_savings(N, X):
    total_income = 2 ** X
    remaining_amount = total_income

    for i in range(1, N + 1):
        expense = remaining_amount // 2
        remaining_amount -= expense

    return remaining_amount

# Input
T = int(input())

for _ in range(T):
    N, X = map(int, input().split())
    amount_saved = calculate_savings(N, X)
    print(amount_saved)
