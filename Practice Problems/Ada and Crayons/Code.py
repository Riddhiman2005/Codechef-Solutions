t = int(input()) 

while t:
    S = input()  

    c = 0  

  
    for i in range(len(S) - 1):
        if S[i] != S[i + 1]:  # Check if the current crayon direction is different from the next
            c += 1  
    
    # Calculate the minimum number of flips needed to make all crayons point in the same direction
    # If the number of segments is even, divide by 2, else divide by 2 and add 1
  
    if c % 2 == 0:
        min_flips = c // 2
    else:
        min_flips = (c // 2) + 1
    
    print(min_flips)  # Print the minimum number of flips 
    
    t -= 1  
