import sys

class InputReader:
    def __init__(self, input_stream):
        self.buffer = input_stream
        self.token = None

    def read_token(self):
        while not self.token:
            line = self.buffer.readline()
            if not line:
                return None
            self.token = iter(line.split())
        return next(self.token)

    def read_int(self):
        return int(self.read_token())

def main():
    sc = InputReader(sys.stdin)
    t = sc.read_int()

    for _ in range(t):
        n = sc.read_int()
        m = sc.read_int()
        x = sc.read_int()
        y = sc.read_int()
        s = sc.read_int()
        r = [0] * (x + 2)
        c = [0] * (y + 2)
        r[-1] = n + 1
        c[-1] = m + 1

        for i in range(1, x + 1):
            r[i] = sc.read_int()

        for i in range(1, y + 1):
            c[i] = sc.read_int()

        x_count = 0
        y_count = 0

        for i in range(1, len(r)):
            x_count += ((r[i] - r[i - 1] - 1) // s)

        for i in range(1, len(c)):
            y_count += ((c[i] - c[i - 1] - 1) // s)

        print(x_count * y_count)

if __name__ == "__main__":
    main()
