t = int(input())  

while t:
    N = int(input())  

    X = list(map(int, input().split()))  # Time taken by Xenny for each task
    Y = list(map(int, input().split()))  # Time taken by Yana for each task

    x = 0
    y = 0

    for i in range(len(X)):
        if i % 2 == 0:
            x += X[i]
            y += Y[i]
        else:
            x += Y[i]
            y += X[i]

    print(min(x, y))  # Print the minimum total time

    t -= 1  
