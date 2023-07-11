# Read the number of rounds
N = int(input())

# Initialize variables
cumulative_score1 = 0
cumulative_score2 = 0
max_lead = 0
winner = 0

# Iterate over the rounds
for _ in range(N):
    # Read the scores of Player 1 and Player 2 in the current round
    score1, score2 = map(int, input().split())

    # Update the cumulative scores
    cumulative_score1 += score1
    cumulative_score2 += score2

    # Calculate the lead for the current round
    lead = abs(cumulative_score1 - cumulative_score2)

    # Check if the lead is greater than the maximum lead
    if lead > max_lead:
        max_lead = lead

        # Determine the winner based on the current round's scores
        if cumulative_score1 > cumulative_score2:
            winner = 1
        else:
            winner = 2

# Print the winner and the maximum lead
print(winner, max_lead)
