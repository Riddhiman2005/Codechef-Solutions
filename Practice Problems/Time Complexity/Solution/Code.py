
# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the number of comparisons used by algorithms A and B
    X, Y = map(int, input().split())
    
    # Check if algorithm A has more time complexity than algorithm B
    if X > Y:
        print("YES")
    else:
        print("NO")
