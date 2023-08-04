# Iterate through each test case
t = int(input())  # Number of test cases
while t:
    # Input for each test case
    N = int(input())  # Number of fingers / sheaths
    L = list(map(int, input().split()))  # Lengths of Chef's fingers
    G = list(map(int, input().split()))  # Lengths of glove sheaths

    a = 0  # Counter for front orientation
    b = 0  # Counter for back orientation

    # Compare finger lengths with sheath lengths
    for i in range(N):
        if L[i] > G[i]:  # Check if finger length exceeds sheath length
            a += 1

        if L[i] > G[N - 1 - i]:  # Check if finger length exceeds sheath length in flipped orientation
            b += 1

    # Determine how Chef can wear the glove
    if a > 0 and b > 0:
        print('none')  # Cannot wear in either orientation
    elif a == 0 and b > 0:
        print('front')  # Can wear with front orientation only
    elif a > 0 and b == 0:
        print('back')  # Can wear with back orientation only
    else:
        print('both')  # Can wear with both orientations

    t -= 1  # Decrement the test case counter
