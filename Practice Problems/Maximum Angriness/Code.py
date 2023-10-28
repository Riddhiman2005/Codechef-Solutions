tc = int(input())
for eachcase in range(tc):
    length, moves = map(int, input().split())
    
    ans = (length * (length - 1)) // 2 # best no. of pairs
    if moves < length // 2:
    
        noswap = length - 2 * moves 
        
        nopairs = (noswap * (noswap - 1)) // 2 
        
        ans = ans - nopairs
    print(ans)
