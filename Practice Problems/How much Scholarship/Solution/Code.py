
# Read the rank
R = int(input())

# Determine the percentage of scholarship
if R <= 50:
    percentage = 100
elif R <= 100:
    percentage = 50
else:
    percentage = 0

# Print the result
print(percentage)
