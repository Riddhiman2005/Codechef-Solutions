t = int(input()) 

while t:
    N = int(input())  # Length of the binary strings

    S = list(input())  # Read the first binary string
    R = list(input())  # Read the second binary string

    # Check if the count of '1's in both strings is the same or not
  
    if S.count('1') == R.count('1'):
        print('YES')  # Possible to change the strings
    else:
        print('NO')  # Not possible to change the strings

    t = t - 1  
