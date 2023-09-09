# cook your dish here
import sys
import queue

t = int(input())

for _ in range(t):
    n = int(input())
    if(n > 1):
        a = [list() for i in range(n)]
        for i in range(n-1):
            line = input().split()
            u = int(line[0]) -1
            v = int(line[1]) -1
            a[u].append(v)
            a[v].append(u)
        q = queue.Queue(n)
        q.put(0)
        V = [False for i in range(n)]
        H = [0 for i in range(n)]
        while(not q.empty()):
            cur = q.get();
            V[cur] = True
            for x in a[cur]:
                if(V[x] == False):
                    q.put(x)
                    H[x] = H[cur] + 1
        H.sort()
        first =0
        last = n-1
        count =0
        turn =0
        while(1):
            if(turn == 0):
                if(first > last):
                    break
                cur = H[first]
                while(H[first] == cur and first <= last):
                    first += 1
                turn = 1
                count = count + 1
            else:
                if(first > last):
                    break
                last = last -1
                count = count +1
                turn = 0
        print(count)
    else:
        if(n ==1):
            print(1)
        else:
            print(0)
