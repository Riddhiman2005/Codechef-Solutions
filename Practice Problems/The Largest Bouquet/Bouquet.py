for t in xrange(int(raw_input())):
    arr=[]
    x=list(map(int,raw_input().split()))
    y=list(map(int,raw_input().split()))
    z=list(map(int,raw_input().split()))
    a=sum(x)
    if a%2==0:
        arr.append(a-1)
    else:
        arr.append(a)
    a=sum(y)
    if a%2==0:
        arr.append(a-1)
    else:
        arr.append(a)
    a=sum(z)
    if a%2==0:
        arr.append(a-1)
    else:
        arr.append(a)
    
    a=x[0]+y[0]+z[0]
    if a%2==0:
        arr.append(a-1)
    else:
        arr.append(a)
        
    a=x[1]+y[1]+z[1]
    if a%2==0:
        arr.append(a-1)
    else:
        arr.append(a)
        
    a=x[2]+y[2]+z[2]
    if a%2==0:
        arr.append(a-1)
    else:
        arr.append(a)
        
    if max(arr)>-1:
        print max(arr)
    else:
        print "0"
