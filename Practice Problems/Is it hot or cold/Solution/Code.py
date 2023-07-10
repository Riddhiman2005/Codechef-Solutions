
def determine_climate(temperature):
    if temperature > 20:
        return "HOT"
    else:
        return "COLD"

# Read the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    # Read the temperature
    temperature = int(input())
    
    # Determine the climate and print the result
    climate = determine_climate(temperature)
    print(climate)
