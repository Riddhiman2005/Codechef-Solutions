def is_chef_likes_match(X, Y):
    # Check if the match ends in a draw and at least one goal is scored by either team
    if X == Y and X > 0:
        return "YES"
    else:
        return "NO"

# Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    X, Y = map(int, input().split())
    result = is_chef_likes_match(X, Y)
    print(result)
