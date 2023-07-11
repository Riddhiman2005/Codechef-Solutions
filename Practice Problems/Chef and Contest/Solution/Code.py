
# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the values of X, Y, P, and Q
    X, Y, P, Q = map(int, input().split())

    # Calculate the penalty time for Chef and Chefina
    chef_penalty = X + (P * 10)
    chefina_penalty = Y + (Q * 10)

    # Determine the winner based on the penalty time
    if chef_penalty < chefina_penalty:
        winner = "Chef"
    elif chef_penalty > chefina_penalty:
        winner = "Chefina"
    else:
        winner = "Draw"

    # Print the winner
    print(winner)
