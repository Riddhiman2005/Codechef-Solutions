
# Read the number of test cases, T
T = int(input())

# Iterate T times
for _ in range(T):
    # Read the number of chocolates, N
    N = int(input())

    # Check if chocolates can be divided equally
    if N % 2 == 0:
        print("Yes")
    else:
        print("No")
