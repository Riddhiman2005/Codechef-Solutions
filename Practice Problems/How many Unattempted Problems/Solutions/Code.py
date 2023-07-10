
# Read the count of all problems and the count of attempted problems
X, Y = map(int, input().split())

# Calculate the number of unattempted problems
unattempted_problems = X - Y

# Print the result
print(unattempted_problems)
