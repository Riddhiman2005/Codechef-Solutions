# Read the number of test cases
T = int(input())

# Iterate over the test cases
for _ in range(T):
    # Read the input for each test case
    N, X, P = map(int, input().split())

    # Calculate the total marks obtained by Chef
    total_marks = (3 * X) + ((N - X) * (-1))

    # Check if Chef passes the exam
    if total_marks >= P:
        print("PASS")
    else:
        print("FAIL")
