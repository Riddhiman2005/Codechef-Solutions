
# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the values of A and C
    A, C = map(int, input().split())
    
    # Check if there exists an integer B
    if (C - A) % 2 != 0:
        print("-1")
    else:
        B = (C + A) // 2
        print(B)
