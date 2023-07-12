# Read the value of T
T = int(input())

# Process each test case
for _ in range(T):
    # Read the value of N
    N = int(input())

    # Read the array A
    A = list(map(int, input().split()))

    # Count the frequency of each element in A
    frequency = {}
    for num in A:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    # Find the maximum frequency
    max_frequency = max(frequency.values())

    # Calculate the minimum number of operations
    min_operations = N - max_frequency

    # Print the result
    print(min_operations)
