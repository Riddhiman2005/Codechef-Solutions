def is_good_permutation(arr):
    inversions = 0
    local_inversions = 0

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                inversions += 1
                if j == i + 1:
                    local_inversions += 1

    return inversions == local_inversions

# Input
T = int(input())

for _ in range(T):
    N = int(input())
    permutation = list(map(int, input().split()))
    result = is_good_permutation(permutation)

    print("YES" if result else "NO")
