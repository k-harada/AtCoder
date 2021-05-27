# https://atcoder.jp/contests/practice/tasks/practice_2


from itertools import permutations, combinations
from collections import deque


class NormalSolver:

    def __init__(self, n, q):
        self.n = n
        self.q = q
        self.size = n
        self.queue = deque()
        for i in range(n):
            self.queue.append("ABCDEFGHIJKLMNOPQRSTUVWXYZ"[i])
        self.x = ""
        self.y = ""
        self.z = ""
        self.running = False
        self.res = ""

    def query(self):
        if self.running:
            # receive result
            if self.res == "<":
                self.z = self.z + self.x[0]
                self.x = self.x[1:]
            else:
                self.z = self.z + self.y[0]
                self.y = self.y[1:]

            # finish merge x and y
            if len(self.x) == 0 or len(self.y) == 0:
                self.z = self.z + self.x + self.y
                self.queue.append(self.z)
                self.z = ""
                self.running = False

        if not self.running:
            if len(self.queue) == 1:
                return "! " + self.queue.pop()
            self.x = self.queue.popleft()
            self.y = self.queue.popleft()
            self.running = True

        return "? " + self.x[0] + " " + self.y[0]

    def input(self, ans):
        self.res = ans


class SpecialSolver:

    def __init__(self, n, q):
        self.n = n
        self.q = q
        self.size = n
        fact_n = 1
        for i in range(n):
            fact_n *= (i + 1)
        i = 1
        while i < fact_n:
            i *= 2
        self.next_n = i
        self.chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:self.n]
        self.candidates = [list(p) for p in permutations(self.chars)]
        self.a = ""
        self.b = ""

    def query(self):
        if len(self.candidates) == 1:
            return "! " + "".join(self.candidates[0])
        self.next_n = self.next_n // 2
        for a, b in combinations(self.chars, 2):
            res_a = 0
            res_b = 0
            for c in self.candidates:
                if c.index(a) < c.index(b):
                    res_a += 1
                else:
                    res_b += 1
            if res_a <= self.next_n and res_b <= self.next_n:
                self.a = a
                self.b = b
                return "? " + a + " " + b
        print(self.next_n, len(self.candidates), "failed")

    def input(self, ans):
        if ans == "<":
            self.candidates = [c for c in self.candidates if c.index(self.a) < c.index(self.b)]
        else:
            self.candidates = [c for c in self.candidates if c.index(self.a) > c.index(self.b)]


def main():
    n, q = map(int, input().split())
    if n == 26:
        solver = NormalSolver(n, q)
    else:
        solver = SpecialSolver(n, q)

    while True:
        res = solver.query()
        if res[0] == "!":
            print(res)
            break
        print(res)
        ans = input()
        solver.input(ans)


if __name__ == "__main__":
    main()
