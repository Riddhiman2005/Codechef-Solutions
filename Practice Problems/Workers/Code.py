def main():
    n = int(input())
    c = list(map(int, input().split()))
    t = list(map(int, input().split()))
    
    tw = 100000
    w = 100000
    tr = 100000
    
    for i in range(n):
        if t[i] == 3:
            if c[i] < tw:
                tw = c[i]
        else:
            if t[i] == 1:
                if c[i] < w:
                    w = c[i]
            if t[i] == 2:
                if c[i] < tr:
                    tr = c[i]
    
    if tw < (tr + w):
        res = tw
    else:
        res = tr + w
    
    print(res)

if __name__ == "__main__":
    main()
