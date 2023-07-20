def is_subset_sum_zero(a, b, c, d):
    # Generate all possible subsets of {a, b, c, d}
    for i in range(1, 16):  # There are 2^4 = 16 possible subsets
        subset_sum = 0
        if i & 1: subset_sum += a
        if i & 2: subset_sum += b
        if i & 4: subset_sum += c
        if i & 8: subset_sum += d
        
        # Check if the subset sum is zero
        if subset_sum == 0:
            return True
            
    return False

# Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    a, b, c, d = map(int, input().split())
    result = is_subset_sum_zero(a, b, c, d)
    print("Yes" if result else "No")
