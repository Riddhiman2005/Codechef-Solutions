t = int(input())
result = []
for i in range(t):
    matrix = []
    n = int(input())
    for j in range(n):          
        temp = list(map(int,input().split()))
        matrix.append(temp)

    flag1,flag2 = 0,0
    for j in range(n):
        if flag1==1 or flag2==1:
            break
        else:
            flag1=1
            flag2=1
            for k in range(n):
                if matrix[k][j]==0:
                    flag1=0
                if matrix[j][k]==0:
                    flag2=0
    if flag1==0 and flag2==0:
        result.append("YES")
    else:
        result.append("NO")
for i in range(t):
    print(result[i])
