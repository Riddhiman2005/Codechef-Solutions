import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Read the number of test cases
T = int(input())

for _ in range(T):
    # Read the coordinates of Alex and Bob
    x1, y1, x2, y2 = map(int, input().split())

    # Calculate the distances of Alex and Bob from Chef
    dist_alex = distance(x1, y1, 0, 0)
    dist_bob = distance(x2, y2, 0, 0)

    # Compare the distances and determine the result
    if dist_alex > dist_bob:
        print("ALEX")
    elif dist_bob > dist_alex:
        print("BOB")
    else:
        print("EQUAL")
