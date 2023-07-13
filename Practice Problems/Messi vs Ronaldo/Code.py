# Read the number of goals and assists for Messi and Ronaldo
A, B, X, Y = map(int, input().split())

# Calculate the total points for Messi and Ronaldo
Messi_points = (22 * A) + (11 * B)
Ronaldo_points = (22 * X) + (11 * Y)

# Compare the total points and output the result
if Messi_points > Ronaldo_points:
    print("Messi")
elif Messi_points < Ronaldo_points:
    print("Ronaldo")
else:
    print("Equal")
