
# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the values of L and R
    L, R = map(int, input().split())

    # Initialize the count of pretty numbers
    count = 0

    # Iterate through the numbers from L to R (inclusive)
    for num in range(L, R+1):
        # Check if the last digit of the number is 2, 3, or 9
        if num % 10 == 2 or num % 10 == 3 or num % 10 == 9:
            count += 1

    # Print the count of pretty numbers
    print(count)
