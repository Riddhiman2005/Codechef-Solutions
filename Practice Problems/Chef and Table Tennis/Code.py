# Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    # Read the binary string S
    S = input()

    # Initialize the score of the Chef and the opponent
    chef_score = 0
    opponent_score = 0

    # Count the points for each player
    for point in S:
        if point == '1':
            chef_score += 1
        else:
            opponent_score += 1

    # Check the conditions to determine the winner
    if chef_score > opponent_score and (chef_score >= 11 or (chef_score == 10 and opponent_score == 10 and chef_score - opponent_score >= 2)):
        print("WIN")
    else:
        print("LOSE")
