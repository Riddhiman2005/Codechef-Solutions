
from collections import deque
import sys


def main():
    t = Iint()
    for _ in range(t):
        n, q = Imap()
        values = Ilist()
        tree = [set() for i in range(n)]
        grandchildren = [list() for i in range(n)]
        for ni in range(n-1):
            u, v = Imap()
            tree[u-1].add(v-1)
            tree[v-1].add(u-1)
        queue = deque([(0, -1)])
        while queue:
            parent, grandparent = queue.pop()
            #debug(parent, grandparent)
            for children in tree[parent]:
                # debug(children)
                tree[children].remove(parent)
                if grandparent != -1:
                    grandchildren[grandparent].append(children)
                queue.append((children, parent))
        # debug(grandchildren)
        # exit()
        for qi in range(q):
            query = Iint()-1
            #debug(query, grandchildren[query])
            if not grandchildren[query]:
                continue
            #debug(values, query)
            queue = deque([query])
            while queue:
                node = queue.pop()
                for g in grandchildren[node]:
                    values[query] += values[g]
                    values[g] = 0
                    queue.append(g)
                grandchildren[node] = []
        Plist(values)


# IO region
FIO = 10


def I(): return input()


def Iint(): return int(input())


def Ilist(): return list(map(int, input().split()))   # int list


def Imap(): return map(int, input().split())   # int map


def Plist(li, s=' '): print(s.join(map(str, li)))   # non string list


# /IO region
en = enumerate


def answer_debug(*args):
    print('\033[31m', *args, '\033[0m', file=sys.stderr)


# answer(9)


def debug(*args):
    print('\033[36m', *args, '\033[0m', file=sys.stderr)


if not FIO:
    if __name__ == '__main__':
        main()
        exit()
else:
    from io import BytesIO, IOBase
    import os
BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)


def input(): return sys.stdin.readline().rstrip("\r\n")



if __name__ == '__main__':
    main()
