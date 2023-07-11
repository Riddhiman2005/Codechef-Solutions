
# Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    # Read the letter class ID
    ID = input()

    # Determine the ship class based on the ID
    if ID == 'B' or ID == 'b':
        print("BattleShip")
    elif ID == 'C' or ID == 'c':
        print("Cruiser")
    elif ID == 'D' or ID == 'd':
        print("Destroyer")
    elif ID == 'F' or ID == 'f':
        print("Frigate")
