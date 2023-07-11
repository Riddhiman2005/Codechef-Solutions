
# Read the input as a single line and split it into two numbers
N1, N2 = map(int, input().split())

# Check if the first number is greater than the second number
if N1 > N2:
    # Calculate and print the difference
    diff = N1 - N2
    print(diff)
else:
    # Calculate and print the sum
    total = N1 + N2
    print(total)
