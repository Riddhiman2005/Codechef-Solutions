def count_subarrays_with_equal_sum_and_product(arr):
    n = len(arr)
    count = 0

    for i in range(n):
        sum_val = 0
        product_val = 1

        for j in range(i, n):
            sum_val += arr[j]
            product_val *= arr[j]

            if sum_val == product_val:
                count += 1

    return count

# Input
T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    # Calculate the number of subarrays with equal sum and product
    result = count_subarrays_with_equal_sum_and_product(A)

    # Print the result for the current test case
    print(result)
