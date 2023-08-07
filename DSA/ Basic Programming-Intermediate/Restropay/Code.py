
n, m, c = map(int, input().split())
tanny_banknotes = list(map(int, input().split()))
purgi_banknotes = list(map(int, input().split()))

# Creating a set of Purgi's banknotes for quick lookup
purgi_banknote_set = set(purgi_banknotes)

# Checking if there is a combination of banknotes that equals the bill
def can_pay_bill(tanny_banknotes, purgi_banknote_set, c):
    for tanny_note in tanny_banknotes:
        required_purgi_note = c - tanny_note
        if required_purgi_note in purgi_banknote_set:
            return True
    return False

# Determining if they can pay the bill using one banknote each

if can_pay_bill(tanny_banknotes, purgi_banknote_set, c):
    print("YES")
else:
    print("NO")
