t = int(input())  # Read the number of test cases

for _ in range(t):
    x = input()  # Read the arrangement of balls in the first row
    y = input()  # Read the arrangement of balls in the second row
    
    n = len(x)  # Calculate the length of the strings
    
    result = ""  # Initialize the result string
    
    # Iterate through the characters of the strings to create the arrangement for row Z
    for i in range(n):
        if x[i] == 'W' and y[i] == 'W':
            result += 'B'
        elif x[i] == 'B' and y[i] == 'B':
            result += 'W'
        else:
            result += 'B'
    
    print(result)  # Print the arrangement of colors for row Z
