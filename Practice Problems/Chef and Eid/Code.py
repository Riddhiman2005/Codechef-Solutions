# Name of the class has to be "Main" only if the class is public.
class Codechef:
    @staticmethod
    def main(args):
        # your code goes here
        t = int(input())

        for _ in range(t):
            n = int(input())
            values = list(map(int, input().split()))

            values.sort()

            min_diff = values[1] - values[0]
            for k in range(n - 1):
                diff = values[k + 1] - values[k]
                if diff < min_diff:
                    min_diff = diff

            print(min_diff)

# Entry point
if __name__ == "__main__":
    codechef = Codechef()
    codechef.main([])
