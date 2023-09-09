from bisect import bisect_left
from re import sub
from typing import DefaultDict
import math
from collections import defaultdict
from math import sqrt
import collections
from sys import maxsize
from itertools import combinations_with_replacement
import sys

def sieve_erasthones(n):
   
    cnt = 0
    prime = [True for i in range(n+1)]
    p = 2
    while (p*p <= n):
        if (prime[p] == True):
            for i in range(p**2, n+1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    for p in range(n+1):
        if prime[p]:
            cnt += 1
    return cnt

def calculate(p, q):
    mod = 998244353
    expo = 0
    expo = mod - 2
    while (expo):
        if (expo & 1):
            p = (p*q) % mod
        q = (q*q) % mod
        expo >>= 1
    return p

def count_factors(n):
    i = 1
    c = 0
    while i <= math.sqrt(n):
        if n % i == 0:
            if n//i == i:
                c += 1
            else:
                c += 2
        i += 1
    return c

def ncr_modulo(n, r, p):
    num = den = 1
    for i in range(r):
        num = (num * (n - i)) % p
        den = (den * (i + 1)) % p
    return (num * pow(den,
                      p - 2, p)) % p

def isprime(n):
    prime_flag = 0
    if(n > 1):
        for i in range(2, int(sqrt(n)) + 1):
            if (n % i == 0):
                prime_flag = 1
                break
        if (prime_flag == 0):
            return True
        else:
            return False
    else:
        return True

def smallestDivisor(n):
    if (n % 2 == 0):
        return 2
    i = 3
    while(i * i <= n):
        if (n % i == 0):
            return i
        i += 2
    return n

def dict_ele_count(l):
    d = DefaultDict(lambda: 0)
    for ele in l:
        d[ele] += 1
    return d

def max_in_dict(d):
    maxi = 0
    for ele in d:
        if d[ele] > maxi:
            maxi = d[ele]
    return maxi

def element_count(s):
    
    l = []
    k = s[0]
    c = 0
    for ele in s:
        if ele == k:
            c += 1
        else:
            l.append([k, c])
            k = ele
            c = 1
    l.append([k, c])
    return l

def modular_exponentiation(x, y, p):
    res = 1
    x = x % p
    if x == 0:
        return 0

    while (y > 0):
        if ((y & 1) != 0):
            res = (res * x) % p
        y = y >> 1
        x = (x * x) % p

    return res

def number_of_primefactor(n):
    l = []
    while n % 2 == 0:
        l.append(2)
        n = n / 2

    for i in range(3, int(math.sqrt(n))+1, 2):
        while (n % i == 0):
            l.append(i)
            n = n / i
    if n > 2:
        l.append(n)
    return len(set(l))

def twosum(a, n, x):
	rem = []
	
	for i in range(x):
		rem.append(0)
	for i in range(n):
		if (a[i] < x):
			rem[a[i] % x] += 1
	for i in range(1, x // 2):
		if (rem[i] > 0 and rem[x - i] > 0):
			return True
	if (i >= x // 2):
		if (x % 2 == 0):
			if (rem[x // 2] > 1):
				return True
			else:
				return False
		else:
			if (rem[x // 2] > 0 and
				rem[x - x // 2] > 0):
				return True
			else:
				return False

def divSum(num) :
    result = 0
    i = 2
    while i<= (math.sqrt(num)) :
        if (num % i == 0) :
            if (i == (num / i)) :
                result = result + i;
            else :
                result = result +  (i + num/i);
        i = i + 1
    return (result + 1 + num)

def solve(): 
    n=int(input())
    l=list(map(int,input().split()))
    k=sum(l)*8
    print(int(math.sqrt(1 +k) -1)//2)
for _ in range(int(input())):
    solve()
