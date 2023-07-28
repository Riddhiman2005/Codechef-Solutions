def can_watch_season(T, test_cases):
    results = []
    for i in range(T):
        M, N, K = test_cases[i]
        total_time = N * K
        if total_time < M:
            results.append("YES")
        else:
            results.append("NO")
    return results

# Input
T = int(input())
test_cases = []
for _ in range(T):
    M, N, K = map(int, input().split())
    test_cases.append((M, N, K))

# Check if Chef can watch Season-1 before the exam starts
results = can_watch_season(T, test_cases)

# Output
for result in results:
    print(result)
