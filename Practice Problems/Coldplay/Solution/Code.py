# Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    # Read the duration of the trip and the duration of the song
    M, S = map(int, input().split())

    # Calculate the number of times the song can be played
    times_played = M // S

    # Print the result
    print(times_played)

