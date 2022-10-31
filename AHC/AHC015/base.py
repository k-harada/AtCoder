import random


class UnionFind:

    def __init__(self, n):
        self.par = [i for i in range(n + 1)]
        self.rank = [0] * (n + 1)

    # search
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    # unite
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    # check
    def same_check(self, x, y):
        return self.find(x) == self.find(y)


uf = UnionFind(100)


def score(state):
    uf.par = [i for i in range(100 + 1)]
    uf.rank = [0] * (100 + 1)
    for i in range(10):
        for j in range(9):
            if state[i][j] == state[i][j + 1]:
                uf.union(i * 10 + j, i * 10 + j + 1)
    for i in range(9):
        for j in range(10):
            if state[i][j] == state[i + 1][j]:
                uf.union(i * 10 + j, i * 10 + j + 10)
    c_list = [0] * 101
    for k in range(100):
        c_list[uf.find(k)] += 1

    s = sum([c ** 2 for c in c_list])
    return s


class Simulator:

    def __init__(self, f_list):
        self.state = [[0] * 10 for _ in range(10)]
        self.t = 0
        self.actions = ["L"] * 100
        self.f_list = [d for d in f_list]

    def set_state(self, state, t):
        self.t = t
        for i in range(10):
            for j in range(10):
                self.state[i][j] = state[i][j]

    def set_actions(self, actions):
        self.actions = [a for a in actions]

    def simulate_once(self):
        for t in range(self.t, 100):
            # 乱数
            k = random.choice(range(100 - t))
            # print(k)
            # 値を埋める
            m = 0
            for i in range(10):
                for j in range(10):
                    if self.state[i][j] == 0:
                        if k == m:
                            self.state[i][j] = self.f_list[t]
                        m += 1
            # 傾ける
            if self.actions[t] == "L":
                for i in range(10):
                    j = 0
                    for k in range(10):
                        if self.state[i][k] != 0:
                            self.state[i][j] = self.state[i][k]
                            j += 1
                    for k in range(j, 10):
                        self.state[i][k] = 0
            elif self.actions[t] == "R":
                for i in range(10):
                    j = 9
                    for k in range(9, -1, -1):
                        if self.state[i][k] != 0:
                            self.state[i][j] = self.state[i][k]
                            j -= 1
                    for k in range(j, -1, -1):
                        self.state[i][k] = 0
            elif self.actions[t] == "F":
                for i in range(10):
                    j = 0
                    for k in range(10):
                        if self.state[k][i] != 0:
                            self.state[j][i] = self.state[k][i]
                            j += 1
                    for k in range(j, 10):
                        self.state[k][i] = 0
            else:
                for i in range(10):
                    j = 9
                    for k in range(9, -1, -1):
                        if self.state[k][i] != 0:
                            self.state[j][i] = self.state[k][i]
                            j -= 1
                    for k in range(j, -1, -1):
                        self.state[k][i] = 0
        # print(self.state)
        # 得点を計算する
        return score(self.state)


class Solver:

    def __init__(self, f_list):
        self.f_list = f_list
        self.f_list.append(1)
        self.t = 0
        self.list_23 = [1] * 101
        self.preprocess()
        self.sm = Simulator(f_list)
        self.actions = self.query_no_look(0)
        self.sm.set_actions(self.actions)
        self.state = [[0] * 10 for _ in range(100)]

    def preprocess(self):
        r_max = 0
        d_max = 0
        for d in range(3):
            res_list = self.query_no_look(d)
            r = res_list.count("F") + res_list.count("B")
            if r > r_max:
                d_max = d
                r_max = r
        self.f_list = [(f + d_max - 1) % 3 + 1 for f in self.f_list]
        return None

    def query_no_look(self, d):
        # d = 0, 1, 2
        res_list = []
        for t in range(100):
            # いちごを優先する
            if self.f_list[t + 1] == (d + 1):
                res = "R"
            # 最新がいちごで次がいちごじゃないときは左に詰める
            elif self.f_list[t + 1] != 1 and self.f_list[t] == (d + 1):
                res = "L"
            # あとは適当に
            else:
                if (self.f_list[t + 1] - (d + 2)) % 3 == 0:
                    res = "F"
                else:
                    res = "B"
            res_list.append(res)
        return res_list

    def query(self, a):
        # 値を埋める
        m = 0
        for i in range(10):
            for j in range(10):
                if self.state[i][j] == 0:
                    if a == m:
                        self.state[i][j] = self.f_list[self.t]
                    m += 1
        # いちごを優先する
        if self.f_list[self.t + 1] == 1:
            res = "R"
        # 最新がいちごで次がいちごじゃないときは左に詰める
        elif self.f_list[self.t + 1] != 1 and self.f_list[self.t] == 1:
            res = "L"
        # あとは適当に
        else:
            if self.t > 1000:  # invalid
                res_b = []
                res_f = []
                self.actions[self.t] = "B"
                for _ in range(100):
                    self.sm.set_state(self.state, self.t)
                    s = self.sm.simulate_once()
                    # print(s)
                    res_b.append(s)
                self.actions[self.t] = "F"
                for _ in range(100):
                    self.sm.set_state(self.state, self.t)
                    s = self.sm.simulate_once()
                    # print(s)
                    res_f.append(s)
                if sum(res_b) <= sum(res_f):
                    res = "F"
                else:
                    res = "B"

            else:
                if self.f_list[self.t + 1] == 2:
                    res = "F"
                else:
                    res = "B"
        # 傾ける
        if res == "L":
            for i in range(10):
                j = 0
                for k in range(10):
                    if self.state[i][k] != 0:
                        self.state[i][j] = self.state[i][k]
                        j += 1
                for k in range(j, 10):
                    self.state[i][k] = 0
        elif res == "R":
            for i in range(10):
                j = 9
                for k in range(9, -1, -1):
                    if self.state[i][k] != 0:
                        self.state[i][j] = self.state[i][k]
                        j -= 1
                for k in range(j, -1, -1):
                    self.state[i][k] = 0
        elif res == "F":
            for i in range(10):
                j = 0
                for k in range(10):
                    if self.state[k][i] != 0:
                        self.state[j][i] = self.state[k][i]
                        j += 1
                for k in range(j, 10):
                    self.state[k][i] = 0
        else:
            for i in range(10):
                j = 9
                for k in range(9, -1, -1):
                    if self.state[k][i] != 0:
                        self.state[j][i] = self.state[k][i]
                        j -= 1
                for k in range(j, -1, -1):
                    self.state[k][i] = 0
        self.t += 1
        return res


def test(index=0, single=True):
    with open(f"./in/{str(10000 + index)[1:]}.txt") as f:
        line = f.readline()
        f_list = list(map(int, line.split()))
        rand_list = []
        for _ in range(100):
            line = f.readline()
            rand_list.append(int(line))

    solver = Solver(f_list)
    score_best = 0
    score_best += f_list.count(1) ** 2
    score_best += f_list.count(2) ** 2
    score_best += f_list.count(3) ** 2

    for t in range(100):
        a = rand_list[t]
        res = solver.query(a)
        if single:
            print(res)
        if t == 99 and not single:
            print(1000000 * score(solver.state) / score_best)


def test_all():
    for i in range(100):
        test(i, single=False)


def main():
    f_list = list(map(int, input().split()))
    solver = Solver(f_list)
    for t in range(100):
        a = int(input())
        res = solver.query(a)
        print(res)


if __name__ == "__main__":
    # test_all()
    main()
