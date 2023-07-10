
# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the number of working hours on each day from Monday to Thursday and Friday
    x, y = map(int, input().split())

    # Calculate the total number of working hours in one week
    total_hours = (x * 4) + y

    # Print the total number of working hours
    print(total_hours)
