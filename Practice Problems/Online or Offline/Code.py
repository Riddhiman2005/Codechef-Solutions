def cheaper_option(N, M):
    online_cost = N - (N * 0.1)  # Applying 10% discount
    if online_cost < M:
        return "ONLINE"
    elif online_cost > M:
        return "DINING"
    else:
        return "EITHER"

# Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    N, M = map(int, input().split())
    print(cheaper_option(N, M))
