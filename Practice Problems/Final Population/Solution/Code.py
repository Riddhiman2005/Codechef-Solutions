
# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the initial population, people leaving, and people immigrating
    x, y, z = map(int, input().split())

    # Calculate the final population
    final_population = x - y + z

    # Print the final population
    print(final_population)
