
T = int(input())  # Read the number of test cases

for _ in range(T):
    A, B = map(int, input().split())  # Read the values of A and B

    time_gap = A + B  # Calculate the time gap between Chef and the winner

    print(time_gap)  # Print the time gap
