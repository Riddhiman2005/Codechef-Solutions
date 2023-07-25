def min_extra_seats(X, Y):
    return max(0, Y - X)

# Input
T = int(input())
for _ in range(T):
    X, Y = map(int, input().split())

    # Calculate the minimum number of extra seats required and print the result
    result = min_extra_seats(X, Y)
    print(result)
