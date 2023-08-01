def is_hard_to_pronounce(S):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    consecutive_consonants = 0

    for char in S:
        if char not in vowels:
            consecutive_consonants += 1
            if consecutive_consonants >= 4:
                return "NO"
        else:
            consecutive_consonants = 0

    return "YES"

# Read the number of test cases (T) from input
T = int(input())

# Process each test case
for _ in range(T):
    # Read the length of the string (N) and the string (S) for each test case
    N = int(input())
    S = input()

    # Check if the string is easy to pronounce and print the result
    print(is_hard_to_pronounce(S))
