
def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y):
    x_root = find(parent, x)
    y_root = find(parent, y)

    if rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
    elif rank[x_root] > rank[y_root]:
        parent[y_root] = x_root
    else:
        parent[y_root] = x_root
        rank[x_root] += 1

# Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    # Read the number of locations and fast roads
    N, M = map(int, input().split())

    parent = list(range(N))
    rank = [0] * N

    # Process the fast roads
    for _ in range(M):
        A, B = map(int, input().split())
        union(parent, rank, A, B)

    # Read the number of queries
    Q = int(input())

    # Process each query
    for _ in range(Q):
        X, Y = map(int, input().split())

        if find(parent, X) == find(parent, Y):
            print("YO")
        else:
            print("NO")
