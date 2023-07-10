
# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the value of A
    a = int(input())

    # Check if Alice likes the number
    if a % 2 == 0 and a % 7 == 0:
        print("Alice")
    # Check if Bob likes the number
    elif a % 2 != 0 and a % 9 == 0:
        print("Bob")
    # If neither Alice nor Bob likes the number, Charlie takes it home
    else:
        print("Charlie")
