# Read the number of test cases
T = int(input())

# Iterate over the test cases
for _ in range(T):
    # Read the values of A and B
    A, B = map(int, input().split())

    # Compare A and B and print the corresponding relational operator
    if A < B:
        print("<")
    elif A > B:
        print(">")
    else:
        print("=")
