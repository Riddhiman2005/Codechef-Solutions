
# Read the number of test cases
T = int(input())

# Iterate over the test cases
for _ in range(T):
    # Read the count of problems and the list of contest codes
    N = int(input())
    contest_codes = input().split()

    # Initialize variables to count the number of problems in each contest
    start38_count = 0
    ltime108_count = 0

    # Iterate over the contest codes and count the occurrences
    for code in contest_codes:
        if code == "START38":
            start38_count += 1
        elif code == "LTIME108":
            ltime108_count += 1

    # Print the counts
    print(start38_count, ltime108_count)
