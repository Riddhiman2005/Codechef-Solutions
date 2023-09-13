# cook your dish here
n = int(input())
grid = []
for k in range(n):
    grid.append([0]*(n))
if n%2 != 0:
    print(-1)
else:
    for x in range(n):
       
        grid[0][x] = x
    for c in range(n):
        if c%2 == 0:
            for r in range(1 , n):
            
                if grid[r-1][c] == 0:
                    grid[r][c] = n - 1 
                    # print(n - 1)
                    # print(grid[r][c] ,grid[r-1][c])
                else:
                    grid[r][c] = grid[r-1][c] - 1 
        else:
            for r in range(1 , n):
    
                if grid[r-1][c] == n - 1:
                    grid[r][c] = 0
                else:
                    grid[r][c] = grid[r-1][c] + 1
                    
    
    for r in grid:
        for c in r:
            print(c , end = " ")
        print()
        
        
    print("R" * (n - 1) , end = "")
    print("D" * (n - 1) , end = "")
    print("L" , end = "")

    counter = 1
    while counter <= n-1:
        if counter%2 == 0:
            print("D" * (n - 2) , end = "")
        else:
            print("U" * (n - 2) , end = "")
        if counter == n-1:
            print("U" , end = "")
        else:
            print("L" , end = "")
        counter += 1 
