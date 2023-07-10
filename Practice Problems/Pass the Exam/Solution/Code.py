
# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the scores in each section
    a, b, c = map(int, input().split())

    # Check the conditions for passing the exam
    if (a + b + c >= 100) and (a >= 10) and (b >= 10) and (c >= 10):
        result = "PASS"
    else:
        result = "FAIL"

    # Print the result
    print(result)
