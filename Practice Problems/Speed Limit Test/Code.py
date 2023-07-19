def who_is_faster(A, X, B, Y):
    speed_alice = A / X
    speed_bob = B / Y
    
    if speed_alice > speed_bob:
        return "ALICE"
    elif speed_alice < speed_bob:
        return "BOB"
    else:
        return "EQUAL"

# Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    A, X, B, Y = map(int, input().split())
    print(who_is_faster(A, X, B, Y))
