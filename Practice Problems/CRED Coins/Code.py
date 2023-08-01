def max_bags_from_store(X, Y):
    # Calculate the total number of CRED coins earned
    total_cred_coins = X * Y

    # Calculate the number of bags Chef can get from the CodeChef store
    max_bags = total_cred_coins // 100

    return max_bags

# Input
T = int(input())

for _ in range(T):
    X, Y = map(int, input().split())
    result = max_bags_from_store(X, Y)
    print(result)
