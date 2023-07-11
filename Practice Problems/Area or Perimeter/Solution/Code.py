
# Read the length and breadth of the rectangle
length = int(input())
breadth = int(input())

# Calculate the area and perimeter
area = length * breadth
perimeter = 2 * (length + breadth)

# Compare the area and perimeter
if area > perimeter:
    print("Area")
    print(area)
elif area < perimeter:
    print("Peri")
    print(perimeter)
else:
    print("Eq")
    print(area)
