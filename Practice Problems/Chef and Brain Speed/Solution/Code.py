
# Read the threshold limit, X, and the current working speed, Y
X, Y = map(int, input().split())

# Check if Chef is prone to errors
if Y > X:
    print("YES")
else:
    print("NO")
