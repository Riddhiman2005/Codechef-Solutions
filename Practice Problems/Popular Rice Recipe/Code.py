# Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    # Read the number of votes
    N = int(input())

    # Initialize a dictionary to store the votes of each user
    votes_dict = {}

    # Iterate through each vote
    for _ in range(N):
        user, vote = input().split()

        # Nullify the previous vote if the user has voted before
        if user in votes_dict:
            previous_vote = votes_dict[user]
            if previous_vote == '+':
                previous_vote = 1
            else:
                previous_vote = -1
            votes_dict[user] = 0

        # Count the latest vote
        if vote == '+':
            votes_dict[user] = '+'
        else:
            votes_dict[user] = '-'

    # Calculate the correct final score
    final_score = sum([1 if vote == '+' else -1 for vote in votes_dict.values()])
    print(final_score)
