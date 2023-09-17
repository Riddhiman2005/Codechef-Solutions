tc=int(input())
while tc>0:
    tc-=1 
    n,k=map(int,input().split())
    min_possible_gcd =(n*(n+1))//2
    if  min_possible_gcd > k:
        print(-1,end=' ')
    elif n==1:
        print(k,end=' ')
    elif min_possible_gcd == k :
        ans=[1]*n
        for each in ans:print(each,end=' ')
    else:
        last_element = k - min_possible_gcd + 1 
        ans=[1]*(n-1)
        ans.append(last_element)
        for each in ans:print(each,end=' ')
    print()
