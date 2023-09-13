# cook your dish here
for _ in range(int(input())):
    msn = int(input())
    mss = input()
    arr = list(mss)
    f = False
    for i in range(msn):
        if f:
            arr[i]="0"
            continue
        if arr[i]=="1" and i<msn-2 :
            f = True
    print(min("".join(arr),mss))
