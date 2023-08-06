def solve(x, k):
    result = False
    divisor = 2
    count = 0
    while divisor * divisor <= x:
        while x % divisor == 0:
            count += 1
            x = x // divisor
        divisor += 1
    if x > 1:
        count += 1
    if count >= k:
        result = True
    return result

t = int(input())
answer = []

for _ in range(t):
    x, k = map(int, input().split())
    if solve(x, k):
        answer.append("1")
    else:
        answer.append("0")

print("\n".join(answer))
