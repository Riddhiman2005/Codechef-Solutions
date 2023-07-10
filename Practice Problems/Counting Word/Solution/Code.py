
T = int(input())  # Read the number of test cases

for _ in range(T):
    N, M = map(int, input().split())  # Read the values of N and M

    total_words = N * M  # Calculate the total number of words in the book

    print(total_words)  # Print the total number of words
