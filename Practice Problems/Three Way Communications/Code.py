import math

# Function to calculate the distance between two points
def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    # Read the communication range
    R = int(input())

    # Read the coordinates of the Chef, head server, and sous-chef
    chef_x, chef_y = map(int, input().split())
    server_x, server_y = map(int, input().split())
    souschef_x, souschef_y = map(int, input().split())

    # Calculate the distances between each pair of people
    chef_server_dist = distance(chef_x, chef_y, server_x, server_y)
    chef_souschef_dist = distance(chef_x, chef_y, souschef_x, souschef_y)
    server_souschef_dist = distance(server_x, server_y, souschef_x, souschef_y)

    # Check if any two people are within direct communication range
    if chef_server_dist <= R and chef_souschef_dist <= R:
        print("yes")
    elif chef_server_dist <= R and server_souschef_dist <= R:
        print("yes")
    elif chef_souschef_dist <= R and server_souschef_dist <= R:
        print("yes")
    else:
        # Check if there is an intermediate person who can establish communication
        if (chef_server_dist + chef_souschef_dist <= 2 * R) or (chef_server_dist + server_souschef_dist <= 2 * R) or (chef_souschef_dist + server_souschef_dist <= 2 * R):
            print("yes")
        else:
            print("no")
