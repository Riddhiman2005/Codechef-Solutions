
# Read the number of test cases
T = int(input())

# Iterate over the test cases
for _ in range(T):
    # Read the salary of the employee
    salary = int(input())

    # Calculate the gross salary based on the given conditions
    if salary < 1500:
        HRA = 0.1 * salary
        DA = 0.9 * salary
    else:
        HRA = 500
        DA = 0.98 * salary

    # Calculate the gross salary
    gross_salary = salary + HRA + DA

    # Print the gross salary
    print("{:.2f}".format(gross_salary))
