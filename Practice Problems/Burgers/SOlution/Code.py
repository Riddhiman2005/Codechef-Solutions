# Read the number of test cases
T = int(input())

# Iterate over the test cases
for _ in range(T):
    # Read the number of patties and buns
    A, B = map(int, input().split())

    # Calculate the maximum number of burgers
    max_burgers = min(A, B, (A + B) // 2)

    # Print the result
    print(max_burgers)
