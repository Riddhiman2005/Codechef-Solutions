
T = int(input())  # Read the number of test cases

for _ in range(T):
    X, Y = map(int, input().split())  # Read the following and follower count of an account

    if X > 10 * Y:
        print("YES")
    else:
        print("NO")
