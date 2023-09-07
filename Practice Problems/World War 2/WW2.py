# cook your dish here

mod=1000000007
def mmul(A,B):
    s=len(A)
    C=[[0 for i in range(s)]for j in range(s)]
    for i in range(s):
        for j in range(s):
            for k in range(s):
                C[i][j]+=(A[i][k]*B[k][j])
                C[i][j]%=mod 
    
    return C 


def mpow(A,N,I):
    if N == 0:
        return I 
    if N==1 :
        return A  
    
    ret=mpow(A,N//2,I)
    ret1=mmul(ret,ret)
    if N%2 == 0:
        return ret1
    else:
        return mmul(ret1,A)
    
t=int(input())
for _ in range(t):
    N,n=[int(c) for c in input().split()]
    I=[[0 for i in range(n)]for j in range(n)]
    
    for i in range(0,n):
        I[i][i] = 1
    
    odd=[[0 for i in range(n)] for j in range(n)]
    even=[[0 for i in range(n)] for j in range(n)]
    
    
    
    for i in range(n):
        odd[i][i] = 1 
        if i >=1 :
            even[i][i-1]=1
            odd[i][i-1]=1 
        if i< n -1 :
            even[i][i+1] =1 
            odd[i][i+1]=1
    
    # print(even)
    # a=mmul(even,I)
    # print(a)
    T=mmul(even,odd)
    N-=1
    ans=mpow(T,N//2,I);
    ret=0;
    if N%2 :
        ans=mmul(ans,even)
    for i in ans:
        for j in i :
            ret+=j
            ret%=mod
    print(ret)    
    
    
    
    


