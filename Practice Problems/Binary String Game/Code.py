def listx():return [int(x) for x in input().split()]
def inpx():return int(input())
def mapx():return map(int,input().split())
def strx():return input()
def floatx():return float(input())

def solve(S):
    N = len(S)
    pos0 = []
    pos1 = []
    for i in range(N):
        if S[i] == '0':
            pos0.append(i)
        elif S[i] == '1':
            pos1.append(i)
        else:
            assert False

    def is_good(num_turns):
        if num_turns * 2 > min(len(pos0), len(pos1)):
            return False
        for c0 in range(num_turns + 1):
            c1 = num_turns - c0
            cur_0 = num_turns + c0 - 1
            cur_1 = len(pos1) - (num_turns + c1)
            p1 = len(pos1) - 1 - (num_turns + c1)
            p0 = num_turns + c0

            num_0 = c0
            num_1 = c1

            split_good = True
            for t in range(num_turns):
                if pos0[cur_0] < pos1[cur_1]:
                    cur_0 -= 1
                    cur_1 += 1
                else:
                    split_good = False
                    break
                if num_1 > 0 and pos0[p0] < pos1[cur_1]:
                    p0 += 1
                    cur_1 += 1
                    num_1 -= 1
                elif num_0 > 0 and pos0[cur_0] < pos1[p1]:
                    cur_0 -= 1
                    p1 -= 1
                    num_0 -= 1
                else:
                    split_good = False
                    break
            if split_good:
                return True
        return False

    mi, ma = 0, len(pos0) // 2 + 1
    while ma - mi > 1:
        md = (mi + ma) // 2
        if is_good(md):
            mi = md
        else:
            ma = md

    return mi

for _ in range(inpx()):
    S = input()
    print(solve(S))


