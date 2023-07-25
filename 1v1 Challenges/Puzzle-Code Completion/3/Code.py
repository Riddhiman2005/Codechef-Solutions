n = int(input())

for i in range(n):
    a, b, c, d = map(int, input().split())
    
    # Calculate the sum of the given angles
    total_sum = a + b + c + d

    # Check if the sum is equal to 360 degrees and if opposite angles sum to 180 degrees
    if total_sum == 360 and a + c == 180 and b + d == 180:
        print("YES")
    else:
        print("NO")
