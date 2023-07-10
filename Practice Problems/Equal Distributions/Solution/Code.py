
T = int(input())  # Read the number of test cases

for _ in range(T):
    A, B = map(int, input().split())  # Read the number of chocolates Alice and Bob have

    if (A + B) % 2 == 0 and abs(A - B) % 2 == 0:
        print("YES")  # Alice and Bob can distribute the chocolates equally
    else:
        print("NO")  # Alice and Bob cannot distribute the chocolates equally
