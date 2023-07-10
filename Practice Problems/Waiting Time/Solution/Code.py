
T = int(input())  # Read the number of test cases

for _ in range(T):
    K, X = map(int, input().split())  # Read the values of K and X for each test case
    remaining_days = (7 * K) - X  # Calculate the number of remaining days Chef has to wait
    
    print(remaining_days)  # Print the number of remaining days for each test case
