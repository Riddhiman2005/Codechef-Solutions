
import math

def shortest_path_length(i, j):
    # Find the common ancestor of nodes i and j
    ancestor = find_common_ancestor(i, j)

    # Calculate the shortest path length
    path_length = get_path_length(i, ancestor) + get_path_length(j, ancestor)

    return path_length

def find_common_ancestor(i, j):
    # Find the common ancestor by finding the highest power of 2
    # that divides both i and j
    while i != j:
        if i > j:
            i = math.floor(i / 2)
        else:
            j = math.floor(j / 2)
    return i

def get_path_length(node, ancestor):
    # Calculate the path length from node to ancestor
    path_length = 0
    while node != ancestor:
        node = math.floor(node / 2)
        path_length += 1
    return path_length

# Read the number of queries
N = int(input())

# Process each query
for _ in range(N):
    # Read the query
    i, j = map(int, input().split())

    # Calculate and print the shortest path length
    print(shortest_path_length(i, j))
