class Solver:

    def __init__(self, n):
        self.n = n
        self.segments = []
        self.d0 = 0
        self.m = 0

    def initialize(self):
        d = 1
        m = 0
        while d <= self.n:
            c = d
            for i in range(1, self.n + 1):
                if i <= c:
                    self.segments.append((i, min(c, self.n)))
                else:
                    self.segments.append((c, i))
                if i - c == d - 1:
                    c += 2 * d
            d *= 2
            m += 1
        self.d0 = d // 2
        self.m = m - 1
        return len(self.segments)

    def query(self, p, q):
        d = self.d0
        v = self.d0
        m = self.m
        while True:
            d //= 2
            if p <= v <= q:
                return m * self.n + p, m * self.n + q
            elif q < v:
                v -= d
            else:
                v += d
            m -= 1


def test():
    n = int(input())
    solver = Solver(n)
    m = solver.initialize()
    print(m)
    for left in range(1, solver.n + 1):
        for right in range(left, solver.n + 1):
            a, b = solver.query(left, right)
            p, q = solver.segments[a - 1]
            r, s = solver.segments[b - 1]
            print(left, right, p, r, q, s)
            assert min(p, r) == left and max(q, s) == right and q >= r


def main():
    n = int(input())
    solver = Solver(n)
    m = solver.initialize()
    print(m)
    for left, right in solver.segments:
        print(f"{left} {right}")

    q = int(input())
    for _ in range(q):
        left, right = map(int, input().split())
        a, b = solver.query(left, right)
        print(f"{a} {b}")
        # print(solver.segments[a - 1])
        # print(solver.segments[b - 1])


if __name__ == "__main__":
    # test()
    main()
