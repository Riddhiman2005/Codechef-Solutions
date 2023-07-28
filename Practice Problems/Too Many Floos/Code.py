def find_floor(room_number):
    return (room_number - 1) // 10 + 1

# Input
T = int(input())
for _ in range(T):
    X, Y = map(int, input().split())

    # Calculate the floor number for Chef and Chefina
    floor_chef = find_floor(X)
    floor_chefina = find_floor(Y)

    # Calculate the number of floors Chef needs to travel
    floors_to_travel = abs(floor_chefina - floor_chef)
    print(floors_to_travel)
