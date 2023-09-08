from sys import stdin, stdout
input = stdin.readline
t = int(input())
for _ in range(t):
    n,m=map(int,input().split())
    ranks=[int(x) for x in input().split()]
    stu=[int(x) for x in input().split()]
    choices=[-1 for i in range(m)]
    for i in range(m):
        choices[i]=[int(x) for x in input().split()]
        choices[i].pop(0)
        choices[i]=choices[i][::-1]
    stud=[]
    for i in range(m):
        stud.append((stu[i],i))
    stud=sorted(stud)
    taken=set()
    chose=0
    for i in stud:
        chose=0
        for j in choices[i[1]]:
            if j not in taken:
                taken.add(j)
                chose=j
                break
        if i[1]==0:
            break
    stdout.write(str(chose)+'\n')
