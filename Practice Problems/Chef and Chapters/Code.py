def total_chapters(X, Y, Z):
    return X * Y * Z

# Input
T = int(input())
for _ in range(T):
    X, Y, Z = map(int, input().split())

    # Calculate the total number of chapters and print the result
    result = total_chapters(X, Y, Z)
    print(result)
