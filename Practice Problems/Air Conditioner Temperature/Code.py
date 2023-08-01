


def can_agree_on_temperature(A, B, C):
    # Find the maximum temperature that satisfies all conditions
    max_temperature = max(A, C)
    
    # Find the minimum temperature that satisfies all conditions
    min_temperature = min(B, max_temperature)
    
    # If the maximum temperature is less than or equal to the minimum temperature, they can agree
    return max_temperature <= min_temperature

# Input
T = int(input())

for _ in range(T):
    A, B, C = map(int, input().split())
    result = can_agree_on_temperature(A, B, C)
    print("Yes" if result else "No")
