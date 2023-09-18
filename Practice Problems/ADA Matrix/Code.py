# cook your dish here
for _ in range(int(input())):
	n = int(input())
	a = [list(map(int,input().split())) for i in range(n)]
	ans = 0;flag = True
	for i in range(n,1,-1):
		for j in range(i-1,0,-1):
			if flag==True:
				if a[i-1][j-1] != (i-1)*n+j:
					ans+=1
					flag = False
			else:
				if a[i-1][j-1] == (i-1)*n+j:
					ans+=1
					flag = True
	print(ans)
