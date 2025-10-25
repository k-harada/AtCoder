class Solver:

    def __init__(self, n):
        self.n = n
        self.i = 0
        self.used = [0] * (2 * n + 2)
        self.used[0] = 1

    def query(self):
        while self.used[self.i] == 1:
            self.i += 1
        self.used[self.i] = 1
        return self.i

    def input(self, r):
        self.used[r] = 1


def main():
    n = int(input())
    solver = Solver(n)
    res = solver.query()
    print(res)
    for i in range(n):
        r = int(input())
        solver.input(r)
        res = solver.query()
        print(res)
    r = int(input())
    assert r == 0


if __name__ == "__main__":
    main()
