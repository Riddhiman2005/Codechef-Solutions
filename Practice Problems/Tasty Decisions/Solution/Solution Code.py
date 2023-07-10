
T = int(input())  # Read the number of test cases

for _ in range(T):
    X, Y = map(int, input().split())  # Read the tastiness of chocolate and candy for each test case
    chocolate_tastiness = 2 * X  # Calculate the total tastiness of one packet of chocolate
    candy_tastiness = 5 * Y  # Calculate the total tastiness of one packet of candy

    if chocolate_tastiness > candy_tastiness:
        print("Chocolate")  # The packet of chocolate is tastier
    elif chocolate_tastiness < candy_tastiness:
        print("Candy")  # The packet of candy is tastier
    else:
        print("Either")  # Both have the same tastiness
