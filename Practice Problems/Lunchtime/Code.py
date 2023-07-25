def is_lunchtime(X):
    return 1 <= X <= 4

# Input
T = int(input())
for _ in range(T):
    X = int(input())

    # Check if it is lunchtime and print the result
    result = "YES" if is_lunchtime(X) else "NO"
    print(result)
