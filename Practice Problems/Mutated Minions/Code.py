# Read the number of test cases
T = int(input())

# Iterate over the test cases
for _ in range(T):
    # Read N and K
    N, K = map(int, input().split())

    # Read the initial characteristic values
    minions = list(map(int, input().split()))

    # Count the number of Wolverine-like minions
    count = 0
    for value in minions:
        # Calculate the new characteristic value
        new_value = value + K

        # Check if the new value is divisible by 7
        if new_value % 7 == 0:
            count += 1

    # Print the result
    print(count)
