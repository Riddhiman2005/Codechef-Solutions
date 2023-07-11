
# Read the value of N
N = int(input())

# Initialize the count of pairs
count = 0

# Iterate through possible values of i
for i in range(1, N // 2 + 1):
    # Calculate j
    j = N - i
    
    # Increment the count of pairs
    count += 1

# Print the number of ordered pairs
print(count)
