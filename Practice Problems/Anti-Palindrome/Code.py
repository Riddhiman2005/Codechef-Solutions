# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    listt=[]
    for i in range(len(s)):
        if (s[i] in listt):
            listt.remove(s[i])
        else:
            listt.append(s[i])
    
            
    a=""
    a+=s[::-1]
    if s==a:
        if len(s)%2==0:
            print(1)
        else:
            print(2)
    else:
        if len(s)%2==0:
            if len(listt)==0:
                print(1)
            else:
                print(0)
        else:
            if len(s)%2==1:
                if len(listt)==1:
                    print(1)
                else:
                    print(0)
                
        
                
            
        
    
