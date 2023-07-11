# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the input values
    A, B, X, Y = map(int, input().split())

    # Calculate the time taken for Chef and Chefina to reach the ground floor
    time_chef = A / X
    time_chefina = B / Y

    # Compare the time values and print the result
    if time_chef < time_chefina:
        print("Chef")
    elif time_chefina < time_chef:
        print("Chefina")
    else:
        print("Both")
