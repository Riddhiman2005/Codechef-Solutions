
T = int(input())  # Read the number of test cases

for _ in range(T):
    N = int(input())  # Read the number of buttons
    initial_states = input()  # Read the initial states of the buttons
    final_states = input()  # Read the final states of the buttons
    
    # If the number of toggles is odd, the bulb state will be reversed
    # If the number of toggles is even, the bulb state will remain the same
    # So, we count the number of differences between initial and final states
    
    num_toggles = sum(1 for i in range(N) if initial_states[i] != final_states[i])
    
    if num_toggles % 2 == 0:
        print("1")  # Bulb state remains the same (on)
    else:
        print("0")  # Bulb state is reversed (off)
