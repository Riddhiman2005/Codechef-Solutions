
# Read the number of test cases
T = int(input())

# Iterate over the test cases
for _ in range(T):
    # Read N, A, B
    N, A, B = map(int, input().split())

    # Read the numbers on the faces of the die
    numbers = list(map(int, input().split()))

    # Count the occurrences of A and B
    count_A = numbers.count(A)
    count_B = numbers.count(B)

    # Calculate the probability of winning
    probability = (count_A * count_B) / (N * N)

    # Print the result
    print(probability)
