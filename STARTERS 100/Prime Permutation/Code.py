# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    if n<4:
        print(-1)
    else:
        c=n//4
        d=c-1
        i,k=1,1
        while k<=d:
            print(i+2,i+3,i,i+1,end=" ")
            k+=1
            i+=4
        k=4+n%4
        if k==4:
            print(i+2,i+3,i,i+1)
        elif k==5:
            print(i+3,i+4,i,i+1,i+2)
        elif k==6:
            print(i+3,i+4,i+5,i,i+1,i+2)
        else:
            print(i+5,i+6,i,i+1,i+2,i+3,i+4)
            
