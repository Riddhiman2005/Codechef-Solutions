def can_defeat_all_enemies(N, H, strengths, resistance):
    for enemy_strength in strengths:
        if enemy_strength <= resistance:
            continue
        elif H > enemy_strength:
            H -= enemy_strength
        else:
            return False
    return True
def find_minimum_resistance(N, H, strengths):
    left, right = 0, max(strengths)
    
    while left < right:
        mid = (left + right) // 2
        
        if can_defeat_all_enemies(N, H, strengths, mid):
            right = mid
        else:
            left = mid + 1
    
    return left
T = int(input())
for _ in range(T):
    N, H = map(int, input().split())
    strengths = list(map(int, input().split()))
    result = find_minimum_resistance(N, H, strengths)
    print(result)
