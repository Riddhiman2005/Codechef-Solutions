t = int(input())

for _ in range(t):
    s = input()  
    
    # Creating a dictionary to store the frequency of each character in the string
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Calculate the sum of frequencies of characters other than the current one
  
    other_sum = sum(value for key, value in char_count.items() if key != s[0])
    
    # Check if the frequency of the current character is equal to the sum of others
  
    if char_count[s[0]] == other_sum:
        print("YES")
    else:
        print("NO")
