def likes_dish(secret_ingredient, threshold):
    for amount in secret_ingredient:
        if amount >= threshold:
            return "YES"
    return "NO"

# Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    # Read N and X
    N, X = map(int, input().split())
    # Read the amount of secret ingredient used by each student
    secret_ingredient = list(map(int, input().split()))
    
    result = likes_dish(secret_ingredient, X)
    print(result)
