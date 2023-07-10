
T = int(input())  # Read the number of test cases

for _ in range(T):
    X, Y = map(int, input().split())  # Read the cost of one special attack and the initial mana points

    max_attacks = Y // X  # Calculate the maximum number of special attacks

    print(max_attacks)  # Print the maximum number of special attacks for the current test case
