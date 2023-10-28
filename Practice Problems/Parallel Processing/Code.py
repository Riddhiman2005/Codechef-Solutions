# cook your dish here
for i in range(int(input())):
    
    a = int(input())
    nums = list(map(int, input().split()))
    
    s1 = sum(nums)
    s2 = 0
    minl = []
    for j in range(a):
        s2 += nums[j]
        s1 -= nums[j]
        minl.append(max(s2,s1))
        
    print(min(minl))
    
    
    
