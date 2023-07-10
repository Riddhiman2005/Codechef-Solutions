
T = int(input())  # Read the number of test cases

for _ in range(T):
    X, Y = map(int, input().split())  # Read the values at which Chef bought and sold the stock

    if Y > X:
        print("PROFIT")
    elif Y < X:
        print("LOSS")
    else:
        print("NEUTRAL")
