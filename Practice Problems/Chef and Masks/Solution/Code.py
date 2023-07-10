
# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the cost of disposable masks and cloth masks
    x, y = map(int, input().split())

    # Calculate the cost of masks for 100 days
    disposable_cost = (x * 100)   # Cost of disposable masks for 100 days
    cloth_cost = (y * 10)         # Cost of cloth masks for 100 days

    # Determine the type of mask Chef will choose
    if cloth_cost <= disposable_cost:
        print("CLOTH")
    else:
        print("DISPOSABLE")
