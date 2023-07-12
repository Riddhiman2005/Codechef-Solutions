
# Read the number of test cases
T = int(input())

# Iterate over the test cases
for _ in range(T):
    # Read the input values
    N = int(input())
    S = input()

    # Initialize an empty string for the encoded sequence
    encoded_sequence = ""

    # Iterate over the binary string in pairs
    for i in range(0, N, 2):
        pair = S[i:i+2]

        # Replace the pair with the corresponding encoded value
        if pair == "00":
            encoded_sequence += "A"
        elif pair == "01":
            encoded_sequence += "T"
        elif pair == "10":
            encoded_sequence += "C"
        elif pair == "11":
            encoded_sequence += "G"

    # Output the encoded sequence
    print(encoded_sequence)
