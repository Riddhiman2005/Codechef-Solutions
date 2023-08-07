
def check_expression(a, b, c, x, y, z):
    return a + x * (b + y * c) == 0


T = int(input())


for _ in range(T):
    A, B, C = map(int, input().split())
    
   
    if check_expression(A, B, C, +1, +1, +1) or \
       check_expression(A, B, C, +1, -1, +1) or \
       check_expression(A, B, C, -1, +1, +1) or \
       check_expression(A, B, C, +1, +1, -1) or \
       check_expression(A, B, C, -1, -1, +1) or \
       check_expression(A, B, C, +1, -1, -1) or \
       check_expression(A, B, C, -1, +1, -1) or \
       check_expression(A, B, C, -1, -1, -1):
        print("YES")
    else:
        print("NO")
