t = int(input())  

for _ in range(t):
    a, b, c, d = map(int, input().split())  # Read the four integers
    
    # Check if a rectangle can be formed with given sides
  
    if (a == b and c == d) or (a == c and b == d) or (a == d and b == c):
        print("YES")  # Rectangle can be formed
    else:
        print("NO")  # Rectangle cannot be formed
