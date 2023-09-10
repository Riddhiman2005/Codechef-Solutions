for i in range(int(input())):
    x=int(input())
    k=x%10
    if(k<5):
        m=x-k
        print(100-m)
    else:
        n=10-k
        p=x+n
        print(100-p)
