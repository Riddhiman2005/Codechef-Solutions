t = int(input())  # Read the number of test cases

for _ in range(t):
    n, k = map(int, input().split())  # Read n and k for the current test case
    minSteps = 0
    low = 0
    high = 0
    
    heights = list(map(int, input().split()))  # Read the heights of the steps
    
    if heights[0] > k:
        if heights[0] % k == 0:
            minSteps += heights[0] // k - 1
        else:
            minSteps += heights[0] // k
    
    for i in range(1, n):
        diff = heights[i] - heights[i - 1]
        if diff > k:
            if diff % k == 0:
                minSteps += diff // k - 1
            else:
                minSteps += diff // k
    
    print(minSteps)  # Print the minimum steps required for the current test case
