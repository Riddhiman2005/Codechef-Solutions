
T = int(input())  # Read the number of test cases

for _ in range(T):
    X, Y = map(int, input().split())  # Read the initial and final volume

    diff = abs(Y - X)  # Calculate the absolute difference between the volumes

    if diff <= 5:
        print(diff)
    else:
        presses = diff // 5
        if diff % 5 != 0:
            presses += 1
        print(presses)
