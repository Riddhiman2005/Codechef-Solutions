from math import *
def f(x, b, c):
	return (x**2 + b*x + c)/sin(x)
def f_d(x, b, c):
	return ((2*x + b)*sin(x) - (x**2 + b*x + c)*cos(x))
def solve(l, h, b, c):
	e = 0.0013
	mid = (l + h)/2
	if abs(f_d(mid, b, c)) < e:
		return mid
	if f_d(mid, b, c) < 0:
		return solve(mid, h, b, c)
	else:
		return solve(l, mid, b, c)
t = int(input())
for i in range(t):
    l = list(map(float, input().rstrip().split()))
    a1 = l[0]
    a2 = l[1]
    mini = solve(0,3.141592/2 , a1, a2)
    print(f(mini, a1, a2))
