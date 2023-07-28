def is_game_interesting(X, Y, D):
    return abs(X - Y) <= D

# Input
T = int(input())
for _ in range(T):
    X, Y, D = map(int, input().split())

    # Check if Chef will find the game interesting
    if is_game_interesting(X, Y, D):
        print("YES")
    else:
        print("NO")
