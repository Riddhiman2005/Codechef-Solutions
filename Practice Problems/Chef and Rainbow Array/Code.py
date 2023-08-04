
t = int(input())  
while t:
    n = int(input()) 
    a = list(map(int, input().split()))  
    r = {1, 2, 3, 4, 5, 6, 7}  
    d = a[::-1]  # Reversing the array 'a'

    # Check if the array is a rainbow or not
    if a == d and set(a) == r:
        print('yes')  # rainbow array
    else:
        print('no')  # not a rainbow array

    t = t - 1  
