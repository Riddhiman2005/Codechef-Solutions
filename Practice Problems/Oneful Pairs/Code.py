# Read the input integers
a, b = map(int, input().split())

# Check if the pair is a Oneful Pair
if a + b + (a * b) == 111:
    print("Yes")
else:
    print("No")
