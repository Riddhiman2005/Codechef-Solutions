import math
def xsum(a,b):
    multiplier=1
    bit_sum=0
    res=0
    while(a or b):
        bit_sum=((a%10) +(b%10))
        bit_sum=bit_sum%10
        res=(bit_sum*multiplier)+res
        a=math.floor(a/10)
        b=math.floor(b/10)
        multiplier=multiplier*10
    return res
for i in range(int(input())):
    a,b=map(int,input().split())
    print(xsum(a,b))
