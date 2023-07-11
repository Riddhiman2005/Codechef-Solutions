from collections import deque

def bfs(group, start):
    visited = set()
    distances = {}
    queue = deque([(start, 0)])

    while queue:
        friend, distance = queue.popleft()

        if friend not in visited:
            visited.add(friend)
            distances[friend] = distance

            for neighbor in group[friend]:
                queue.append((neighbor, distance + 1))

    return distances

# Read the number of groups
num_groups = int(input())

for _ in range(num_groups):
    # Read the friends in the group
    num_friends = int(input())
    group = {}

    # Read the friend lists for each friend in the group
    for i in range(num_friends):
        friends_list = list(map(int, input().split()))
        group[i + 1] = friends_list

    min_average_distance = float('inf')
    most_popular_friend = -1

    # Calculate the average distance for each friend
    for friend in range(1, num_friends + 1):
        distances = bfs(group, friend)
        total_distance = sum(distances.values())
        average_distance = total_distance / num_friends

        if average_distance < min_average_distance:
            min_average_distance = average_distance
            most_popular_friend = friend

    # Print the most popular friend and their average distance
    print(most_popular_friend, "{:.6f}".format(min_average_distance))
