# Read the number of test cases

T = int(input())

# Iterate over each test case
for _ in range(T):
    # Read the number of cards
    N = int(input())

    # Read the numbers written on the cards
    A = list(map(int, input().split()))

    # Create a frequency dictionary
    freq = {}
    for num in A:
        freq[num] = freq.get(num, 0) + 1

    # Find the maximum frequency
    max_freq = max(freq.values())

    # Calculate the minimum number of moves
    min_moves = N - max_freq

    # Print the minimum number of moves
    print(min_moves)
