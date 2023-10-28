for i in range (int(input())):
    n = int(input())
    if(360%n==0 and n<=360):
        print("y ",end = '')
    else:
        print("n ",end = '')
    if(n<=360):
        print("y ",end = '')
    else:
        print("n ",end = '')
    if((n*(n+1))/2 <= 360):
        print("y ", end = '')
    else:
        print("n ", end ='')
    print("\n")
        
