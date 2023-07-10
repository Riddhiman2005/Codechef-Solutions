
# Read the number of soldiers
n = int(input())

# Read the number of weapons each soldier is holding
weapons = list(map(int, input().split()))

# Count the number of lucky and unlucky soldiers
lucky_count = 0
unlucky_count = 0

# Iterate through each soldier
for soldier in weapons:
    # Check if the soldier is lucky or unlucky based on the number of weapons
    if soldier % 2 == 0:
        lucky_count += 1
    else:
        unlucky_count += 1

# Check if the army is ready for battle
if lucky_count > unlucky_count:
    print("READY FOR BATTLE")
else:
    print("NOT READY")
