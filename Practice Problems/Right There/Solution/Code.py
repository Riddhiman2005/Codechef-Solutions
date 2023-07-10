
T = int(input())  # Read the number of test cases

for _ in range(T):
    N, X = map(int, input().split())  # Read the total number of people and the capacity of the party hall

    if N <= X:  # Check if the total number of people is less than or equal to the capacity of the party hall
        print("YES")  # Chef can host the party
    else:
        print("NO")  # Chef cannot host the party
