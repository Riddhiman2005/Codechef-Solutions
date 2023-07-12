
# Read the number of test cases
T = int(input())

# Iterate over the test cases
for _ in range(T):
    # Read the number of songs in Vlad's playlist
    N = int(input())

    # Read the lengths of the songs
    songs = list(map(int, input().split()))

    # Read the position of "Uncle Johny"
    K = int(input())

    # Get the length of "Uncle Johny" in the initial playlist
    uncle_johny_length = songs[K-1]

    # Sort the list of songs
    sorted_songs = sorted(songs)

    # Find the position of "Uncle Johny" in the sorted playlist
    position = sorted_songs.index(uncle_johny_length) + 1

    # Print the position
    print(position)
