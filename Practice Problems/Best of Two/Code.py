# Read the number of test cases
T = int(input())

# Iterate over the test cases
for _ in range(T):
    # Read the dice rolls for Alice and Bob
    a1, a2, a3, b1, b2, b3 = map(int, input().split())

    # Calculate the scores for Alice and Bob
    alice_score = sum(sorted([a1, a2, a3])[1:])
    bob_score = sum(sorted([b1, b2, b3])[1:])

    # Compare the scores and determine the winner or tie
    if alice_score > bob_score:
        print("Alice")
    elif alice_score < bob_score:
        print("Bob")
    else:
        print("Tie")
