
# Read the number of test cases, T
T = int(input())

# Iterate T times
for _ in range(T):
    # Read the values of X and Y
    X, Y = map(int, input().split())

    # Check if Y falls within the recommended range
    if Y >= X and Y <= X + 200:
        print("YES")
    else:
        print("NO")
