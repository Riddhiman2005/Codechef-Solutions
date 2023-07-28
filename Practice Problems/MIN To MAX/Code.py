def min_operations_to_max(T, test_cases):
    results = []
    for i in range(T):
        N, A = test_cases[i]
        M = min(A)
        max_val = max(A)
        operations = max_val - M
        results.append(operations)
    return results

# Input
T = int(input())
test_cases = []
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    test_cases.append((N, A))

# Find the minimum number of operations for each test case
results = min_operations_to_max(T, test_cases)

# Output
for result in results:
    print(result)
