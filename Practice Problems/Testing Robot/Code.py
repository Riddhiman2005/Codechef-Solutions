t = int(input()) 

while t:
    N, X = map(int, input().split())  # Read N and X
    S = input()  # Read the string S

    arr = []
    arr.append(X)  # Initial position

    for i in S:
        if i == 'R':
            X += 1
            arr.append(X)
        
        if i == 'L':
            X -= 1
            arr.append(X)
    
    arr = set(arr)  # Remove duplicates by converting to set
    print(len(arr))  # Print the number of distinct points visited

    t -= 1  
