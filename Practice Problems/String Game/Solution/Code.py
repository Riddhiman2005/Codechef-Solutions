
def determine_winner(binary_string):
    count = 0
    for i in range(len(binary_string) - 1):
        if binary_string[i] != binary_string[i + 1]:
            count += 1

    if count % 2 == 0:
        return "Ramos"
    else:
        return "Zlatan"

# Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    # Read the length of the binary string
    N = int(input())

    # Read the binary string
    binary_string = input()

    # Determine the winner and print the result
    winner = determine_winner(binary_string)
    print(winner)
