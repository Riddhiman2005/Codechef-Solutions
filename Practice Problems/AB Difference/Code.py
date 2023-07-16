# Read the input values
A, B = map(int, input().split())

# Calculate the correct answer and Chef's output
correct_answer = A + B
chef_output = A * B

# Calculate the absolute difference
difference = abs(correct_answer - chef_output)

# Print the difference
print(difference)
