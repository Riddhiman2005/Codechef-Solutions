t = int(input())  

while t:
    n = str(input())  
    for i in list(n):  
        # Check if the count of the current character equals the sum of counts of other characters
        if n.count(i) == (len(n) - n.count(i)):
            print("YES")  # Print "YES" if the condition is satisfied
            break  # Exit the loop since the condition is met
    else:
        print("NO")  # Print "NO" if the loop completes without finding a character that satisfies the condition
    
    t = t - 1  
