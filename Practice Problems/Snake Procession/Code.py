t = int(input())  

while t:
    R = int(input())  # Length of the report
    L = input()       # String representing the report
    L = L.replace('.', '')  # Remove the '.' characters from the report

    k = 0
    for i in range(0, len(L), 2):
        if L[i:i+2] != "HT":
            print("Invalid")
            k = 1
            break
    
    if k == 0:
        print("Valid")

    t = t - 1
