n = int(input())

for i in range(n):
    a, b = map(int, input().split())

    # Calculate the time required to make one doughnut
    time_for_one_doughnut = 3 * b

    # Calculate the maximum number of doughnuts that can be made in time N
    doughnuts_ready = a // time_for_one_doughnut

    print(doughnuts_ready)
