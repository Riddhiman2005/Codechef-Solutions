def is_eligible_team(n):
    return 6 <= n <= 8

# Read the input
n = int(input())

# Check if the team is eligible and print the result
if is_eligible_team(n):
    print("Yes")
else:
    print("No")
