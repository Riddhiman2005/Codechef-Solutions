# Read the number N from the user
N = int(input())

# Convert the number to a string and get its length
num_length = len(str(N))

# Check the length and print the corresponding message
if num_length == 1:
    print("1")
elif num_length == 2:
    print("2")
elif num_length == 3:
    print("3")
else:
    print("More than 3 digits")
