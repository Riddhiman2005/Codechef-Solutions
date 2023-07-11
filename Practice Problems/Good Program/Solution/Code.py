# cook your dish here
# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the number of bits taken by the program
    N = int(input())
    
    # Check if the number of bits is a multiple of 4
    if N % 4 == 0:
        print("Good")
    else:
        print("Not Good")
