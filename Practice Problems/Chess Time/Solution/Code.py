
T = int(input())  # Read the number of test cases

for _ in range(T):
    N = int(input())  # Read the number of hours of free time

    games = (N * 60) // 20  # Calculate the maximum number of complete chess games

    print(games)  # Print the result
