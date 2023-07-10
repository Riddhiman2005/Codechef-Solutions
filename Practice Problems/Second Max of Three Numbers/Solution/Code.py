N = int(input())  # Read the number of triples

for _ in range(N):
    nums = list(map(int, input().split()))  # Read the three integers as a list

    second_max = sorted(nums)[-2]  # Sort the list and get the second maximum number
    print(second_max)  # Print the second maximum number
