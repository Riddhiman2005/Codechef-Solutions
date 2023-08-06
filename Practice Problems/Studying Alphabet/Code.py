S = input()  # String of letters Jeff can read
t = int(input())  # Number of words in the book

while t:
    x = True
    word = input()  
    
    
    for i in word:
        if i not in S:  
            x = False  # If a character is not in Jeff's set, mark x as False
            break  # Exit the loop early since the word cannot be read
    
    # Print 'Yes' if Jeff can read the word, otherwise print 'No'
    if x:
        print('Yes')
    else:
        print('No')

    t = t - 1  
