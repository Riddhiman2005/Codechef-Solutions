
T = int(input())  # Read the number of test cases

for _ in range(T):
    stats_A = list(map(int, input().split()))  # Read the stats for player A
    stats_B = list(map(int, input().split()))  # Read the stats for player B
    
    count_A = 0  # Counter for player A's better stats
    count_B = 0  # Counter for player B's better stats
    
    for i in range(3):
        if stats_A[i] > stats_B[i]:
            count_A += 1
        else:
            count_B += 1
    
    if count_A > count_B:
        print("A")
    else:
        print("B")
