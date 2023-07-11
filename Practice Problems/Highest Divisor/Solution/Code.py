
# Read the input
N = int(input())

# Initialize the largest divisor as 1
largest_divisor = 1

# Check divisors from 10 to 1
for i in range(10, 0, -1):
    if N % i == 0:
        largest_divisor = i
        break

# Print the largest divisor
print(largest_divisor)
