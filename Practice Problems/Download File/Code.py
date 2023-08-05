t = int(input())  
while t:
    N, K = map(int, input().split())  # Reading N and K for the current test case

    s = 0  # Initializing the total cost 's' for the current test case

    for n in range(N):
        T, D = map(int, input().split())  # Reading T and D for each internet data usage entry
        
        if K != 0:  # If free minutes left
            if K >= T:  # If the remaining free minutes are greater than or equal to T
                K -= T
                T = 0
            else:
                T -= K
                K = 0

        s += T * D  # Calculate and add the cost for the current usage
        
    print(s)  # Print the total cost 
    t -= 1  
