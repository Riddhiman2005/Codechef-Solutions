# cook your dish here
def get_chunks(s, x):
    chunk_sizes = list()
    curr_chunk = 0

    for ch in s:
        if ch == x:
            if curr_chunk != 0:
                chunk_sizes.append(curr_chunk)
                curr_chunk = 0
        else:
            curr_chunk += 1

    if curr_chunk != 0:
        chunk_sizes.append(curr_chunk)

    return chunk_sizes
for _ in range(int(input())):
    n = int(input())
    s, x = input().strip().split(' ')

    chunk_sizes = get_chunks(s, x)

    total = n*(n+1) / 2
    no_x = 0
    for sz in chunk_sizes:
        no_x += (sz * (sz + 1) / 2)

    print(int(total - no_x))
