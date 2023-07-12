# Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    # Read the number N
    N = int(input())

    # Convert the number to a string
    number_str = str(N)

    # Reverse the string
    reversed_str = number_str[::-1]

    # Check if the number is a palindrome
    if number_str == reversed_str:
        print("wins")
    else:
        print("loses")
