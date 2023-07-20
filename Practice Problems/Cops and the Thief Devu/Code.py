def is_house_safe(thief_position, cop_positions, x, y):
    for cop_position in cop_positions:
        distance = abs(thief_position - cop_position)
        max_distance = x * y
        if distance <= max_distance:
            return False
    return True

def count_safe_houses(N, cop_positions, x, y):
    safe_houses = 0
    for house in range(1, N+1):
        if is_house_safe(house, cop_positions, x, y):
            safe_houses += 1
    return safe_houses

# Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    M, x, y = map(int, input().split())
    cop_positions = list(map(int, input().split()))
    N = 100  # Total number of houses
    safe_houses = count_safe_houses(N, cop_positions, x, y)
    print(safe_houses)
