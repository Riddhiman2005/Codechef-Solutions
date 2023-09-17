# cook your dish here
def main():
    t = int(input())
    for i in range(t):
        n,h,y1,y2,l = map(int,input().split())
        cross = 0
        for j in range(n):
            ti,x = map(int,input().split())
            if l == 0:
                continue
            if ti == 1:
                if h-y1 <= x:
                    cross += 1
                elif l > 0:
                    l -= 1
                    if l > 0:
                        cross += 1
            else:
                if y2 >= x:
                    cross += 1
                elif l > 0:
                    l -= 1
                    if l > 0:
                        cross += 1

        print(cross)

main()
