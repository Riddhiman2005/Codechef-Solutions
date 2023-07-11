
# Read the number of test cases
T = int(input())

# Iterate over each test case
for _ in range(T):
    # Read the year
    N = int(input())

    # Check if SnackDown was hosted in the year
    if N in [2010, 2015, 2016, 2017, 2019]:
        print("HOSTED")
    else:
        print("NOT HOSTED")
