
# Process each test case
while True:
    # Read n
    n = int(input())

    # Check if the test case is the last one
    if n == 0:
        break

    # Read the permutation
    permutation = list(map(int, input().split()))

    # Check if the permutation is ambiguous
    is_ambiguous = True
    for i in range(n):
        if permutation[permutation[i] - 1] != i + 1:
            is_ambiguous = False
            break

    # Print the result
    if is_ambiguous:
        print("ambiguous")
    else:
        print("not ambiguous")
