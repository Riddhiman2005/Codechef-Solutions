# cook your dish here
# cook your dish here
n = int(input())
type__ = int(input())

out = []
curr = n

from functools import lru_cache

@lru_cache(maxsize = None)
def put(i):
    global curr
    
    out.append(f'put {i}')
    curr += 1
    return curr - 1


def putnew(i):
    global curr
    
    out.append(f'put {i}')
    curr += 1
    return curr - 1

@lru_cache(maxsize = None)
def compose(i):
    global curr

    out.append(f'compose {i}')
    curr += 1
    return curr - 1

def compnew(i):
    global curr

    out.append(f'compose {i}')
    curr += 1
    return curr - 1

@lru_cache(maxsize = None)
def add(i, j):
    global curr
    
    out.append(f'add {i} {j}')
    curr += 1
    return curr - 1

def addnew(i, j):
    global curr
    
    out.append(f'add {i} {j}')
    curr += 1
    return curr - 1

def echo(i):
    return add(i, put(0))
    
@lru_cache(maxsize = None)
def compare(i, j):
    global curr
    
    out.append(f'compare {i} {j}')
    curr += 1
    return curr - 1

@lru_cache(maxsize = None)
def mult(i, j):
    global curr
    
    out.append(f'multiply {i} {j}')
    curr += 1
    return curr - 1

@lru_cache(maxsize = None)
def sub(i, j):
    global curr
    
    out.append(f'subtract {i} {j}')
    curr += 1
    return curr - 1

def cswap(i, j):
    #print('cswap',i,j)
    
    cmp = compare(j, i)

    #diff = sub(i, j)
    #chng = mult(cmp, diff)
    chng = sub(mult(cmp, i), mult(cmp, j))

    global res
    res = add(cmp, res)

    f = sub(i, chng)
    s = add(chng, j)

    return (f, s)

res = put(0)

ct = 0
def solve(i, j):
    global res
    global ct
    #ct += 1

    sz = j - i

    if sz == 1:
        loc = put(i)
        compose(loc)
        putnew(n)

        #print('Returning:',i,j,loc + 1, loc + 3)
        return (loc + 1, loc + 3)

    if sz <= 4:
        curr = list(range(i, j))

        for _ in range(sz - 1):
            for ind in range(sz - _ - 1):
                curr[ind], curr[ind + 1] = cswap(curr[ind], curr[ind + 1])

        inic = []

        for v in curr:
            inic.append(echo(v))
        inic.append(putnew(n))

        #print('Returning:',i,j,min(inic), max(inic) + 1)
        return (min(inic), max(inic) + 1)

    #assert sz != 10
    
    szh = sz//2 if sz not in [10] else 4        

    i1, j1 = solve(i, i + szh)
    i2, j2 = solve(i + szh, j)

    left = put(i1) #pointer
    right = put(i2) #pointer
    
    #comp(left) = left_ind

    #print(i, j, left, right)

    things = []
    for it in range(sz):
        #print(left, right)
        
        ct += 1
        
        u = compose(left)
        v = compose(right)
        #print(i, j, u, v)
        assert v == u + 1
        
        cmp = compare(compose(right), compose(left))
        cmpinv = compare(compose(left), compose(right))
        #print('comp',cmp, compinv)

        res = add(res, mult(cmp, sub(put(j1 - 1), left)))

        #print('res',res)

        left = add(left, cmpinv)
        right = add(right, cmp)

        lloc = add(put(u), cmp)
        things.append(lloc)

    inic = []

    if sz < 5000:
        for v in things:
            inic.append(compnew(v))
            
    inic.append(putnew(n))

    #print('Returning:',i,j,min(inic), max(inic) + 1)
    return (min(inic), max(inic) + 1)
    
solve(0, n)

'''
solve(0, 1000)

vv = 1000000

for n in range(2, 20):
    vv += 1000000
    out = []
    solve(vv, vv + n)
    print(n, len(out))
for n in range(2, 20):
    vv += 1000000
    out = []
    solve(vv, vv + n)
    print(n, len(out))'''

compnew(put(res))

print(len(out))
print('\n'.join(out))
