
# Read the number of test cases
T = int(input())

# Iterate over each test case
for _ in range(T):
    # Read Utkarsh's preference order
    preference = input().split()

    # Read the offers Utkarsh has received
    offers = input().split()

    # Check which offer Utkarsh will accept based on preference
    if preference[0] in offers:
        accepted_company = preference[0]
    elif preference[1] in offers:
        accepted_company = preference[1]
    else:
        accepted_company = preference[2]

    # Print the accepted company
    print(accepted_company)
