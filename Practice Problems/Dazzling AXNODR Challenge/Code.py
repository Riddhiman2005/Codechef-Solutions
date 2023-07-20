def find_beauty(N):
    beauty = 1
    for i in range(2, N + 1):
        if i % 2 == 0:
            beauty = beauty ^ i
        else:
            beauty = beauty & i
    return beauty

# Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    # Read N
    N = int(input())

    # Find the beauty of the canvas for the current test case
    result = find_beauty(N)
    print(result)
