
# Read the number of problems solved in each week
p1, p2, p3, p4 = map(int, input().split())

# Initialize a counter for the number of weeks Chef met his target
weeks_met_target = 0

# Check each week if Chef met his target of solving at least 10 problems
if p1 >= 10:
    weeks_met_target += 1
if p2 >= 10:
    weeks_met_target += 1
if p3 >= 10:
    weeks_met_target += 1
if p4 >= 10:
    weeks_met_target += 1

# Print the number of weeks Chef met his target
print(weeks_met_target)
