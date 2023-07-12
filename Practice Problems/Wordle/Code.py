
# Read the number of test cases
T = int(input())

# Iterate over the test cases
for _ in range(T):
    # Read the hidden word and guess word
    hidden_word = input().strip().upper()
    guess_word = input().strip().upper()

    # Initialize the result string
    result = ""

    # Compare each character of the hidden word with the guess word
    for i in range(len(hidden_word)):
        if hidden_word[i] == guess_word[i]:
            result += 'G'
        else:
            result += 'B'

    # Print the result string
    print(result)
