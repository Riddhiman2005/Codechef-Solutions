# Read the input
R, O, C = map(int, input().split())

# Calculate the maximum possible score for Team B in the remaining overs
max_possible_score = (20 - O) * 6 * 6

# Check if Team B can win the match
if C + max_possible_score > R:
    print("YES")
else:
    print("NO")
