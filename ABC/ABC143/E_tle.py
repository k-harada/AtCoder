from collections import deque


class SolveE:

    def __init__(self, n, le):
        self.n = n
        self.le = le
        self.g1 = [[] for _ in range(n)]
        self.g2 = [[] for _ in range(n)]

    def add_edge(self, a, b, c):
        self.g1[a].append([b, c])

    def pre_compute(self):
        for i in range(self.n):
            d_list = [self.le + 1] * self.n
            d_list[i] = 0
            queue = deque([i])
            while len(queue) > 0:
                p = queue.popleft()
                for q, r in self.g1[p]:
                    if d_list[q] > d_list[p] + r and d_list[p] + r <= self.le:
                        d_list[q] = d_list[p] + r
                        queue.append(q)
            for j in range(self.n):
                if 0 < d_list[j] <= self.le:
                    self.g2[i].append(j)

    def query(self, s, t):
        d_list = [10000] * self.n
        d_list[s] = 0
        queue = deque([s])
        while len(queue) > 0:
            p = queue.popleft()
            for q in self.g2[p]:
                if q == t:
                    return d_list[p] + 1
                if d_list[q] > d_list[p] + 1:
                    d_list[q] = d_list[p] + 1
                    queue.append(q)
        return 0


def main():
    n, m, le = map(int, input().split())
    sol = SolveE(n, le)
    for _ in range(m):
        a, b, c = map(int, input().split())
        if c <= le:
            sol.add_edge(a - 1, b - 1, c)
            sol.add_edge(b - 1, a - 1, c)

    sol.pre_compute()

    q = int(input())
    res_list = [0] * q
    for i in range(q):
        s, t = map(int, input().split())
        res = sol.query(s - 1, t - 1)
        res_list[i] = res - 1

    for r in res_list:
        print(r)


if __name__ == "__main__":
    main()
