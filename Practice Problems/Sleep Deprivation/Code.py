def is_sleep_deprived(X):
    if X < 7:
        return "YES"
    else:
        return "NO"

# Input
T = int(input())
for _ in range(T):
    X = int(input())

    # Check if Chef is sleep-deprived and print the result
    result = is_sleep_deprived(X)
    print(result)
