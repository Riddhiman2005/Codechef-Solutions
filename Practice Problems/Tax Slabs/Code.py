for _ in range(int(input())):
    n = int(input())
    tax = 0
    if (n >= 0) and (n <= 250000):
            tax = (0*n)
    elif (n > 250000) and (n <= 500000):
        tax = (0.05 * (n-250000))
    elif (n > 500000) and (n <= 750000):
        tax = ((0.05 * (500000-250000)) + (0.1*(n-500000)))
    elif (n > 750000) and (n <= 1000000):
        tax = ((0.05 * (500000-250000)) + (0.1*(750000-500000)) + (0.15*(n-750000)))
    elif (n > 1000000) and (n <= 1250000):
        tax = ((0.05 * (500000-250000)) + (0.1*(750000-500000)) + (0.15*(1000000-750000)) + (0.20*(n-1000000)))
    elif (n > 1250000) and (n <= 1500000):
        tax = ((0.05 * (500000-250000)) + (0.1*(750000-500000)) + (0.15*(1000000-750000)) + (0.20*(1250000-1000000)) + (0.25*(n-1250000)))
    elif (n > 1500000):
        tax = ((0.05 * (500000-250000)) + (0.1*(750000-500000)) + (0.15*(1000000-750000)) + (0.20*(1250000-1000000)) + (0.25*(1500000-1250000)) + (0.30*(n-1500000))) 
    print(int(n-tax))