
# Read the number of integers
T = int(input())

# Iterate over the integers
for _ in range(T):
    # Read each integer from the list
    num = int(input())

    # Convert the integer to a string and count occurrences of '4'
    count = str(num).count('4')

    # Print the count
    print(count)
