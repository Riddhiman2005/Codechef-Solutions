
# Read the number of test cases, T
T = int(input())

# Iterate T times
for _ in range(T):
    # Read the number of candies, N
    N = int(input())

    # Check if the number of candies can be distributed equally
    if N % 3 == 0:
        print("YES")
    else:
        print("NO")
