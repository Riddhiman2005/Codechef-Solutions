
def is_lucky_number(N):
    power_of_two = 0
    while N % 2 == 0:
        N //= 2
        power_of_two += 1
    return power_of_two % 2 == 0

T = int(input())


for _ in range(T):
    N = int(input())
    if is_lucky_number(N):
        print(1)
    else:
        print(0)
