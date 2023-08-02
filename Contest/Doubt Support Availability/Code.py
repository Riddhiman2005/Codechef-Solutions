def has_doubt_support(difficulty):
    if difficulty <= 1600:
        return "Yes"
    else:
        return "No"

# Read the input
difficulty = int(input())

# Determine if the problem has Doubt Support
result = has_doubt_support(difficulty)

# Print the result
print(result)
