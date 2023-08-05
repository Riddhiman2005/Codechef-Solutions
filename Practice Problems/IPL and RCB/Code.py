t = int(input()) 

while t:
    X, Y = map(int, input().split())  
    if X > Y:
        print(X - Y)  # If RCB has more points than matches remaining, print the difference
    else:
        print(0)  # Otherwise, RCB already has enough points to qualify, so print 0
        
    t = t - 1  
