# Read the values of N and Q
N, Q = map(int, input().split())

# Read the array of N roots
roots = list(map(int, input().split()))

# Process each query
for _ in range(Q):
    # Read the query value
    x = int(input())

    # Calculate the product of differences
    product = 1
    for root in roots:
        product *= (x - root)

    # Determine the value of the polynomial
    if product > 0:
        print("POSITIVE")
    elif product < 0:
        print("NEGATIVE")
    else:
        print("0")
