def is_happy(X, Y):
    if X >= 2 * Y:
        return "Yes"
    else:
        return "No"

# Input
X, Y = map(int, input().split())

# Output
result = is_happy(X, Y)
print(result)
