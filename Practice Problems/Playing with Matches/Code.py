
t = int(input()) 

M = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]  # List containing the number of matches needed for digits 0 to 9

while t:
    A, B = map(int, input().split())  
    m = 0  
    S = str(A + B)  # Calculate the sum of A and B, and convert it to a string
    for i in S:
        i = int(i)  # Convert the character to an integer
        m = m + M[i]  # Add the number of matches needed for this digit
        
    print(m)  # Print the total number of matches needed

    t = t - 1  
