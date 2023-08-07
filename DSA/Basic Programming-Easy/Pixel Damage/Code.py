import math


def is_distance_less_than_K(H, W, X, Y, K):
    distance_to_bottom_right = math.sqrt((H - Y)**2 + (W - X)**2)
    return distance_to_bottom_right < K


T = int(input())


for _ in range(T):
    H, W, X, Y, K = map(int, input().split())
    if is_distance_less_than_K(H, W, X, Y, K):
        print(1)
    else:
        print(0)
