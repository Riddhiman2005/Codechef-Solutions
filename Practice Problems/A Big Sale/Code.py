t = int(input())  

while t:
    N = int(input())  
    dis = 0.0  
    for j in range(N):
        P, Q, D = map(float, input().split())  
      
        # Final price after the discount
        p = P + (P * (D / 100))
        p = p - (p * (D / 100))

        # LOss for this recipe type and add it to the total loss
        loss = (P - p) * Q
        dis = dis + loss

    print("{:.2f}".format(dis)) 
    t = t - 1  
