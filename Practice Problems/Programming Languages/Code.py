
# Read the number of test cases
T = int(input())

# Iterate over the test cases
for _ in range(T):
    # Read the features of the required language and the available languages
    A, B, A1, B1, A2, B2 = map(int, input().split())

    # Check if the required features are present in the first language
    if (A == A1 or A == B1) and (B == A1 or B == B1):
        print(1)
    # Check if the required features are present in the second language
    elif (A == A2 or A == B2) and (B == A2 or B == B2):
        print(2)
    # Neither language has all the required features
    else:
        print(0)
