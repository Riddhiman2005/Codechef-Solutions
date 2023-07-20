def count_jewel_stones(jewels, stones):
    count = 0
    for stone in stones:
        if stone in jewels:
            count += 1
    return count

# Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    # Read the jewel and stone strings
    jewels = input()
    stones = input()

    # Find the number of jewel stones
    result = count_jewel_stones(jewels, stones)
    print(result)
