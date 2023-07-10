
T = int(input())  # Read the number of test cases

for _ in range(T):
    N, X, Y = map(int, input().split())  # Read the values of N, X, and Y for each test case
    total_size = X + 2 * Y  # Calculate the total size of the files
    
    if total_size <= N:  # Check if the total size is less than or equal to the available space
        print("YES")  # Print "YES" if Chef can save the files
    else:
        print("NO")  # Print "NO" if Chef cannot save the files
