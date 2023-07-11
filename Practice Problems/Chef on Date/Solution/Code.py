
# Read the number of test cases, T
T = int(input())

# Iterate T times
for _ in range(T):
    # Read the amount of money Chef has, X, and the bill amount, Y
    X, Y = map(int, input().split())

    # Check if Chef has enough money to pay the bill
    if X >= Y:
        print("YES")
    else:
        print("NO")
