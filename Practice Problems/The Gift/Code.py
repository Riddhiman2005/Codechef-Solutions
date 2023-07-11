# Read the input values
X, N, M = map(int, input().split())

# Check if Om can buy the laptop
if X >= N or (X + M) >= N:
    print("YES")
else:
    print("NO")
