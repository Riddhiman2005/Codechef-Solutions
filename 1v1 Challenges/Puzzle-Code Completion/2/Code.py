a,b=map(int,input().split())



#  Calculate the time to reach the rest point at normal pace
time_to_rest_point_normal_pace = b

# Calculate the time to reach the rest point at twice the normal pace
time_to_rest_point_twice_pace = b // 2

# Calculate the remaining distance after the rest point
remaining_distance = a - b

# Calculate the time to cover the remaining distance at normal pace
time_after_rest_point_normal_pace = remaining_distance

# Calculate the total travel time
total_travel_time = time_to_rest_point_twice_pace + time_after_rest_point_normal_pace

print(total_travel_time)
