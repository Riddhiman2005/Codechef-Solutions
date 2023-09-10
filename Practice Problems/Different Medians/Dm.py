import sys
from os import path
if(path.exists('Input.txt')):
    sys.stdin = open("Input.txt","r")
    sys.stdout = open("Output.txt","w")

import math
from collections import deque
def solve():
	n=int(input())
	q=deque()
	for i in range(1,n+1):
		q.append(i)
	for ii in range(n):
		if(ii%2==0):
			print(q.pop(),end=" ")
		else:
			print(q.popleft(),end=" ")
	print()
		
for _ in range(int(input())):
	solve()
