import time
import numpy as np
t_zero = time.time()


def input_data():
    ml, il, rl, bl, cl = map(int, list(input().split())[1:])

    bom = np.zeros((ml, il), dtype=np.int32)
    com = np.zeros((ml, il, il), dtype=np.int32)
    order = np.zeros((rl, 6), dtype=np.int32)

    # BOM
    for _ in range(bl):
        i, m, s = map(int, list(input().split())[1:])
        bom[m, i] = s

    # COM
    for _ in range(cl):
        m, i_pre, i_next, t = map(int, list(input().split())[1:])
        com[m, i_pre, i_next] = t

    # ORDER
    for _ in range(rl):
        r, i, e, d, q, pr, a = map(int, list(input().split())[1:])
        order[r, 0] = i
        order[r, 1] = e
        order[r, 2] = d
        order[r, 3] = q
        order[r, 4] = pr
        order[r, 5] = a

    return ml, il, rl, bom, com, order


class Solver:

    m = 1
    i = 3
    r = 3

    bom = np.array([[10, 10, 10]])
    com = np.array([[[0, 30, 20], [30, 0, 20], [10, 20, 0]]])
    order = np.array([
        [0, 0, 60, 1, 100, 1000],
        [0, 0, 60, 1, 100, 1000],
        [1, 0, 60, 1, 100, 1000],
        [1, 0, 120, 1, 100, 1000],
        [2, 0, 120, 1, 100, 1000],
        [2, 0, 120, 1, 100, 1000]
    ])

    def __init__(self):
        self.assign_list = [[] for _ in range(self.m)]
        self.t_last = np.zeros(self.m, dtype=np.int32)
        self.p_last = -1 * np.ones(self.m, dtype=np.int32)

    def init_list(self, assign_list):
        self.assign_list = assign_list

    def insert_last(self, r):
        m_min = -1
        t_min = 10000000000
        i = self.order[r, 0]
        e = self.order[r, 1]
        q = self.order[r, 3]

        for m in range(self.m):
            if self.bom[m, i] == 0:
                continue
            t = self.t_last[m]
            p = self.p_last[m]
            t1 = max(t, e)
            if p == -1:
                t2 = t1
            else:
                t2 = t1 + self.com[m, p, i]
            t3 = t2 + self.bom[m, i] * q
            if t3 < t_min:
                m_min = m
                t_min = t3

        self.assign_list[m_min].append(r)
        self.t_last[m_min] = t_min
        self.p_last[m_min] = i

    def print_current_plan(self):
        self.print_plan(self.assign_list)

    def score_current_plan(self):
        return self.score_plan(self.assign_list)

    @classmethod
    def score_one_list(cls, m, assign):
        sub_score = 0
        t = 0
        p = -1
        for r in assign:
            i = cls.order[r, 0]
            e = cls.order[r, 1]
            d = cls.order[r, 2]
            q = cls.order[r, 3]
            pr = cls.order[r, 4]
            a = cls.order[r, 5]
            t1 = max(t, e)
            if p == -1:
                t2 = t1
            else:
                t2 = t1 + cls.com[m, p, i]
            t3 = t2 + cls.bom[m, i] * q

            # update
            p = i
            t = t3

            # score
            delay = max(0, t3 - d)
            pe1 = (pr * delay + (a - 1)) // a
            pe2 = t2 - t1

            sub_score += pr - pe1 - pe2
        return sub_score

    @classmethod
    def score_plan(cls, assign_list):
        profit = 10 ** 10
        t_array = np.zeros(cls.m, dtype=np.int32)
        p_array = -1 * np.ones(cls.m, dtype=np.int32)
        for m in range(cls.m):
            for r in assign_list[m]:
                i = cls.order[r, 0]
                e = cls.order[r, 1]
                d = cls.order[r, 2]
                q = cls.order[r, 3]
                pr = cls.order[r, 4]
                a = cls.order[r, 5]

                t1 = max(t_array[m], e)
                if p_array[m] == -1:
                    t2 = t1
                else:
                    t2 = t1 + cls.com[m, p_array[m], i]
                t3 = t2 + cls.bom[m, i] * q

                # update
                p_array[m] = i
                t_array[m] = t3

                # score
                delay = max(0, t3 - d)
                pe1 = (pr * delay + (a - 1)) // a
                pe2 = t2 - t1

                profit += pr - pe1 - pe2

        return profit

    @classmethod
    def print_plan(cls, assign_list):
        t_array = np.zeros(cls.m, dtype=np.int32)
        p_array = -1 * np.ones(cls.m, dtype=np.int32)
        for m in range(cls.m):
            for r in assign_list[m]:
                i = cls.order[r, 0]
                e = cls.order[r, 1]
                # d = cls.order[r, 2]
                q = cls.order[r, 3]
                # pr = cls.order[r, 4]
                # a = cls.order[r, 5]

                t1 = max(t_array[m], e)
                if p_array[m] == -1:
                    t2 = t1
                else:
                    t2 = t1 + cls.com[m, p_array[m], i]
                t3 = t2 + cls.bom[m, i] * q
                # assert t3 > t2

                # update
                p_array[m] = i
                t_array[m] = t3

                print(r, m, t1, t2, t3)

        return None


if __name__ == "__main__":
    M, I, R, BOM, COM, ORDER = input_data()
    Solver.m = M
    Solver.i = I
    Solver.r = R
    Solver.bom = BOM
    Solver.com = COM
    Solver.order = ORDER

    solver_1 = Solver()
    solver_2 = Solver()
    orders_1 = sorted([(r, Solver.order[r, 2]) for r in range(Solver.r)], key=lambda x: x[1])
    orders_2 = sorted([(r, Solver.order[r, 1]) for r in range(Solver.r)], key=lambda x: x[1])
    for i in range(Solver.r):
        solver_1.insert_last(orders_1[i][0])
        solver_2.insert_last(orders_2[i][0])
    # print(solver_1.score_current_plan(), solver_2.score_current_plan())
    if solver_1.score_current_plan() > solver_2.score_current_plan():
        solver_1.print_current_plan()
    else:
        solver_2.print_current_plan()
