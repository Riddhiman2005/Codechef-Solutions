def is_good_weather(days):
    sunny_days = days.count(1)
    rainy_days = days.count(0)
    return sunny_days > rainy_days

# Input
T = int(input())
test_cases = []
for _ in range(T):
    days = list(map(int, input().split()))
    test_cases.append(days)

# Check if the weather report is Good for each testcase
results = []
for days in test_cases:
    result = "YES" if is_good_weather(days) else "NO"
    results.append(result)

# Output
for result in results:
    print(result)
