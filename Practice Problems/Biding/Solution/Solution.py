
T = int(input())  # Read the number of test cases

for _ in range(T):
    A, B, C = map(int, input().split())  # Read the amount bid by Alice, Bob, and Charlie

    if A > B and A > C:
        print("Alice")  # Alice has the highest bid
    elif B > A and B > C:
        print("Bob")  # Bob has the highest bid
    else:
        print("Charlie")  # Charlie has the highest bid
