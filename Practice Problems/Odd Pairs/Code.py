def count_pairs_with_odd_sum(N):
    return (N * N) // 2

# Input
T = int(input())
for _ in range(T):
    N = int(input())

    # Find the number of required pairs
    result = count_pairs_with_odd_sum(N)

    # Print the result for the current test case
    print(result)
