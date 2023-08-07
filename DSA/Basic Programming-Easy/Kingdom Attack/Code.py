
def second_smallest(arr):
    smallest = second_smallest = float('inf')
    
    for num in arr:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num
            
    return second_smallest


T = int(input())


for _ in range(T):
    N = int(input())
    temperature_forecast = list(map(int, input().split()))
    
    second_coldest_day = second_smallest(temperature_forecast)
    print(second_coldest_day)
