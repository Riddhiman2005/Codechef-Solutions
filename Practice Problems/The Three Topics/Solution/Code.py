
# Read the topics Chef has prepared and the given topic
A, B, C, X = map(int, input().split())

# Check if Chef has any chances of winning the contest
if X in [A, B, C]:
    print("Yes")
else:
    print("No")
