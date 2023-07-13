# Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    # Read the number of workers
    N = int(input())

    # Read the salaries of the workers
    salaries = list(map(int, input().split()))

    # Find the minimum salary
    min_salary = min(salaries)

    # Calculate the total number of operations
    total_operations = sum(s - min_salary for s in salaries)

    # Output the minimum number of operations
    print(total_operations)
