def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def game_termination_value(arr):
    n = len(arr)
    gcd = arr[0]
    for i in range(1, n):
        gcd = find_gcd(gcd, arr[i])

    return gcd

# Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    # Read the array length and elements
    N = int(input())
    A = list(map(int, input().split()))

    # Find and print the game termination value
    result = game_termination_value(A)
    print(result)
