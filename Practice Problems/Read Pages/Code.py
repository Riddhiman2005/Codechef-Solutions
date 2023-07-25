def can_complete_book(N, X, Y):
    return X * Y >= N

# Input
T = int(input())

for _ in range(T):
    N, X, Y = map(int, input().split())

    # Check if Chef can complete the book and print the result
    result = "YES" if can_complete_book(N, X, Y) else "NO"
    print(result)
