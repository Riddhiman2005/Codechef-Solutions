
T = int(input())  # Read the number of test cases

for _ in range(T):
    N = int(input())  # Read the number of test cases in the current test case
    sizes = list(map(int, input().split()))  # Read the sizes of the test cases
    verdicts = input()  # Read the binary string representing the verdicts
    
    min_size = float('inf')  # Initialize the minimum size with infinity
    
    for i in range(N):
        if verdicts[i] == '0':
            min_size = min(min_size, sizes[i])
    
    print(min_size)
