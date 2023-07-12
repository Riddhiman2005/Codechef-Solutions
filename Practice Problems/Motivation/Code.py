
# Read the number of test cases
T = int(input())

# Iterate over the test cases
for _ in range(T):
    # Read the number of movies and the available space
    N, X = map(int, input().split())

    # Initialize the highest rating
    highest_rating = 0

    # Iterate over each movie
    for _ in range(N):
        # Read the space required and the IMDB rating of the movie
        S, R = map(int, input().split())

        # Check if the movie fits within the available space
        if S <= X:
            # Update the highest rating if necessary
            highest_rating = max(highest_rating, R)

    # Print the highest rating of a movie that can fit in the hard disk
    print(highest_rating)
