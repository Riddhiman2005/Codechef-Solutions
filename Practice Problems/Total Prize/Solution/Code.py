
# Read the number of test cases
T = int(input())

# Iterate over the test cases
for _ in range(T):
    # Read the prize for top 10 rankers and ranks 11 to 100
    X, Y = map(int, input().split())

    # Calculate the total prize money
    total_prize = (10 * X) + (90 * Y)

    # Print the total prize money
    print(total_prize)
