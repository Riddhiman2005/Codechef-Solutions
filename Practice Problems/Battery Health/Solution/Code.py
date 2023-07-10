
T = int(input())  # Read the number of test cases

for _ in range(T):
    X = int(input())  # Read the battery health

    if X >= 80:  # Check if battery health is 80% or above
        print("YES")  # Battery is in optimal condition
    else:
        print("NO")  # Battery is not in optimal condition
