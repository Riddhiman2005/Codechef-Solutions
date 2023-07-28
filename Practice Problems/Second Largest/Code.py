def find_second_largest(a, b, c):
    numbers = [a, b, c]
    numbers.sort()
    return numbers[1]

# Input
T = int(input())
for _ in range(T):
    A, B, C = map(int, input().split())

    # Find the second largest number
    second_largest = find_second_largest(A, B, C)

    # Output
    print(second_largest)
