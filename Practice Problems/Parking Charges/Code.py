
def calculate_parking_charges(x, y, h):
    if h <= 1:
        return x
    else:
        extra_hours = h - 1
        total_charges = x + (extra_hours * y)
        return total_charges

# Read the input values
x, y, h = map(int, input().split())

# Calculate and print the total parking charges
total_charges = calculate_parking_charges(x, y, h)
print(total_charges)
