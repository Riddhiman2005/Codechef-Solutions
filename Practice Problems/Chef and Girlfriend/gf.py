for _ in range(int(input())):
    t1=[float(x) for x in input().split(":")]
    t1=t1[0]*60+t1[1]
    t2=[float(x) for x in input().split(":")]
    t2=t2[0]*60+t2[1]
    dist=float(input())
    print(round(t1-t2+dist,1),end=" ")
    if 2*dist>t1-t2:
        print(round(dist+(t1-t2)/2,1))
    else:
        print(round(t1-t2,1))
