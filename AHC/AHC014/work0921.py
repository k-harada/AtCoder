import numpy as np


class Solver:

    def __init__(self, n, m, xy_list):
        self.n = n
        self.field = np.zeros((n, n, 9), dtype=int)
        for x, y in xy_list:
            self.field[x, y, 0] = 1
        self.initialize()

    def initialize(self):
        # 1 up
        for i in range(self.n):
            r = -1
            for j in range(self.n - 1, -1, -1):
                self.field[i, j, 1] = r
                if self.field[i, j, 0] == 1:
                    r = j
        # 2 down
        for i in range(self.n):
            r = -1
            for j in range(self.n):
                self.field[i, j, 2] = r
                if self.field[i, j, 0] == 1:
                    r = j
        # 3 right
        for j in range(self.n):
            r = -1
            for i in range(self.n - 1, -1, -1):
                self.field[i, j, 3] = r
                if self.field[i, j, 0] == 1:
                    r = i

        # 4 left
        for j in range(self.n):
            r = -1
            for i in range(self.n):
                self.field[i, j, 4] = r
                if self.field[i, j, 0] == 1:
                    r = i

        return None

    def add_node(self, i, j, direction):
        # add
        x, y = self._add_node(i, j, direction)
        if x == -1:
            return ""

        # disable edge
        x0, x1, y0, y1 = min(i, x), max(i, x), min(j, y), max(j, y)
        self._disable_rect(x0, x1, y0, y1)
        self._update_new(i, j, direction)

        return f"{i} {j} {x} {j} {x} {y} {i} {y}"

    def _add_node(self, i, j, direction):

        if self.field[i, j, 0] == 1:
            return -1, -1

        # up - right
        if direction == 0:
            x = self.field[i, j, 3]
            y = self.field[i, j, 1]
            if self.field[i, y, 3] == x and self.field[x, j, 1] == y and x >= 0 and y >= 0:
                # add node
                self.field[i, j, 0] = 1
                return x, y

        # up - left
        elif direction == 1:
            x = self.field[i, j, 4]
            y = self.field[i, j, 1]
            if self.field[i, y, 4] == x and self.field[x, j, 1] == y and x >= 0 and y >= 0:
                # add node
                self.field[i, j, 0] = 1
                return x, y

        # down - left
        elif direction == 2:
            x = self.field[i, j, 4]
            y = self.field[i, j, 2]
            if self.field[i, y, 4] == x and self.field[x, j, 2] == y and x >= 0 and y >= 0:
                # add node
                self.field[i, j, 0] = 1
                return x, y

        # down - right
        elif direction == 3:
            x = self.field[i, j, 3]
            y = self.field[i, j, 2]
            if self.field[i, y, 3] == x and self.field[x, j, 2] == y and x >= 0 and y >= 0:
                # add node
                self.field[i, j, 0] = 1
                return x, y

        return -1, -1

    def _disable_rect(self, x0, x1, y0, y1):
        # x0
        self.field[x0, y0:y1, 1] = -1
        self.field[x0, (y0 + 1):(y1 + 1), 2] = -1
        # x1
        self.field[x1, y0:y1, 1] = -1
        self.field[x1, (y0 + 1):(y1 + 1), 2] = -1
        # y0
        self.field[x0:x1, y0, 3] = -1
        self.field[(x0 + 1):(x1 + 1), y0, 4] = -1
        # y1
        self.field[x0:x1, y1, 3] = -1
        self.field[(x0 + 1):(x1 + 1), y1, 4] = -1

        return None

    def _update_new(self, i, j, direction):
        # up
        if direction == 0 or direction == 1:
            for y in range(j - 1, -1, -1):
                self.field[i, y, 1] = j
                if self.field[i, y, 0] == 1:
                    break
        else:
            # down
            for y in range(j + 1, self.n):
                self.field[i, y, 2] = j
                if self.field[i, y, 0] == 1:
                    break

        # right
        if direction == 0 or direction == 3:
            for x in range(i - 1, -1, -1):
                self.field[x, j, 3] = i
                if self.field[x, j, 0] == 1:
                    break
        else:
            # right
            for x in range(i + 1, self.n):
                self.field[x, j, 4] = i
                if self.field[x, j, 0] == 1:
                    break

        return None


def solve(n, m, xy_list):
    res = []
    solver = Solver(n, m, xy_list)
    for _ in range(40):
        add = 0
        for i in range(n):
            for j in range(n):
                for direction in range(4):
                    s = solver.add_node(i, j, direction)
                    if len(s):
                        add += 1
                        # print(i, j, direction)
                        res.append(s)
        if add == 0:
            break
    return res


def main():
    n, m = map(int, input().split())
    xy_list = [tuple(map(int, input().split())) for _ in range(m)]
    res = solve(n, m, xy_list)
    print(len(res))
    for r in res:
        print(r)


def test_seed_0():
    res = solve(33, 58, [
        (13, 24), (14, 24), (15, 24), (16, 24), (17, 24), (12, 23), (18, 23), (11, 22), (19, 22), (10, 21),
        (20, 21), (9, 20), (21, 20), (8, 19), (15, 19), (18, 19), (22, 19), (8, 18), (12, 18), (15, 18),
        (18, 18), (22, 18), (8, 17), (12, 17), (15, 17), (18, 17), (22, 17), (8, 16), (12, 16), (15, 16),
        (18, 16), (22, 16), (8, 15), (12, 15), (15, 15), (18, 15), (22, 15), (9, 14), (12, 14), (15, 14),
        (18, 14), (21, 14), (10, 13), (12, 13), (15, 13), (18, 13), (20, 13), (22, 13), (11, 12), (12, 12),
        (15, 12), (18, 12), (19, 12), (23, 12), (12, 11),
        (15, 11), (18, 11), (24, 11)
    ])
    print(len(res))
    for r in res:
        print(r)


if __name__ == "__main__":
    # test_seed_0()
    main()
