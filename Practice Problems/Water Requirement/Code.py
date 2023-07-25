def water_required(N):
    return 2 * N

# Input
T = int(input())
for _ in range(T):
    N = int(input())

    # Calculate the total amount of water required and print the result
    result = water_required(N)
    print(result)
