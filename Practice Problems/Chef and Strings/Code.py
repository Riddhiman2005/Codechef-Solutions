# Read the number of test cases
T = int(input())

# Iterate over the test cases
for _ in range(T):
    # Read the number of times Chef has to pluck a string
    N = int(input())

    # Read the string numbers
    string_numbers = list(map(int, input().split()))

    # Initialize the total skips to 0
    total_skips = 0

    # Iterate over the string numbers and calculate the skips
    for i in range(N - 1):
        skips = abs(string_numbers[i] - string_numbers[i+1]) - 1
        total_skips += skips

    # Print the total number of skips
    print(total_skips)
