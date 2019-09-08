from time import time as time_stamper
import numpy as np

t_zero = time_stamper()
# t -> 1000t
LARGE = 240 * 1000 + 1


class Solver:

    K = 0
    L = 0

    t_on = np.zeros(K, dtype=np.int32)
    t_off = np.zeros(K, dtype=np.int32)
    p_names = [""] * K

    t_stay = np.zeros(L, dtype=np.int32)
    r_by = np.zeros(L, dtype=np.int32)
    d_names = [""] * L

    a_mat = np.zeros((K, K), dtype=np.int32)
    b_mat = np.zeros((L, K), dtype=np.int32)
    c_mat = np.zeros((L, L), dtype=np.int32)

    def __init__(self, initial_tour):

        self.tour = initial_tour.copy()
        self.best_tour = initial_tour.copy()
        s = self.score_tour(initial_tour)
        self.score = s
        self.best_score = s

    @classmethod
    def update_dim(cls):
        cls.t_on = np.zeros(cls.K, dtype=np.int32)
        cls.t_off = np.zeros(cls.K, dtype=np.int32)
        cls.p_names = [""] * cls.K

        cls.t_stay = np.zeros(cls.L, dtype=np.int32)
        cls.r_by = np.zeros(cls.L, dtype=np.int32)
        cls.d_names = [""] * cls.L

        cls.a_mat = np.zeros((cls.K, cls.K), dtype=np.int32)
        cls.b_mat = np.zeros((cls.L, cls.K), dtype=np.int32)
        cls.c_mat = np.zeros((cls.L, cls.L), dtype=np.int32)

    def fit_car(self, tour):

        dp = np.ones((self.K, 10), dtype=np.int32) * LARGE
        # initialize
        dp[:, 0] = self.t_off + self.b_mat[tour[0], :]
        dp_arr_from = -1 * np.ones((self.K, self.L), dtype=np.int32)
        dp_arr_when = -1 * np.ones((self.K, self.L), dtype=np.int32)

        res = self.t_stay[tour[0]]

        # update
        for jj in range(1, self.L):
            j_ = jj % 10

            when_v = dp.argmin(axis=1)
            # distance + to
            dist_m = self.a_mat + self.b_mat[tour[jj], :] + self.t_off
            # from
            dist_m += (dp.min(axis=1) + self.b_mat[tour[jj - 1], :] + self.t_on)[:, np.newaxis]
            dist_m -= self.c_mat[tour[jj - 1], tour[jj]]

            dp[:, j_] = dist_m.min(axis=0)
            dp_arr_from[:, jj] = dist_m.argmin(axis=0)
            dp_arr_when[:, jj] = when_v[dp_arr_from[:, jj]]

            res += self.c_mat[tour[jj - 1], tour[jj]]
            res += self.t_stay[tour[jj]]

        # trajectory from reverse direction
        trajectory = []
        arg_m = dp.argmin()
        tp_, tf = arg_m % 10, arg_m // 10
        tp = self.L
        tp -= ((tp - tp_ - 1) % 10 + 1)
        trajectory.append([tp, tf])
        while tp > 0:
            tp_, tf = dp_arr_when[tf, tp], dp_arr_from[tf, tp]
            tp -= ((tp - tp_ - 1) % 10 + 1)
            trajectory.append([tp, tf])

        return list(reversed(trajectory))

    def score_tour(self, tour):

        time_passed = 0

        trajectory = self.fit_car(tour)

        time_vec = np.zeros(self.L, dtype=np.int32)

        for ii in range(len(trajectory) - 1):
            t1, p1 = trajectory[ii]
            t2, p2 = trajectory[ii + 1]

            time_passed += self.t_off[p1]
            time_passed += self.b_mat[tour[t1], p1]

            for t in range(t1, t2):
                time_passed += self.t_stay[tour[t]]
                time_vec[t] = time_passed
                if t + 1 < t2:
                    time_passed += self.c_mat[tour[t], tour[t + 1]]
            time_passed += self.b_mat[tour[t2 - 1], p1]
            time_passed += self.t_on[p1]
            time_passed += self.a_mat[p1, p2]

        # last
        tl, pl = trajectory[-1]
        time_passed += self.t_off[pl]
        time_passed += self.b_mat[tour[tl], pl]
        for t in range(tl, self.L):
            time_passed += self.t_stay[tour[t]]
            time_vec[t] = time_passed
            if t + 1 < self.L:
                time_passed += self.c_mat[tour[t], tour[t + 1]]

        r_by_tour = self.r_by[tour]
        # base score
        s = 240 * 60
        s += 10000 * (time_vec <= 240 * 1000).sum()
        # late penalty
        v = np.maximum(time_vec - r_by_tour, 0)
        s -= 100000 * (v > 0).sum()
        s -= v.sum()
        # total time penalty
        s -= time_vec[-1] * 60 // 1000
        return s

    def update_tour(self, tour, tour_score):
        self.tour = tour.copy()
        self.score = tour_score
        if tour_score > self.best_score:
            self.best_tour = tour.copy()
            self.best_score = tour_score

    def print_best_tour(self):

        # fit car
        trajectory = self.fit_car(self.best_tour)
        res_str = [""] * len(trajectory)

        for ii in range(len(trajectory) - 1):
            t1, p1 = trajectory[ii]
            t2, p2 = trajectory[ii + 1]
            res_str[ii] = " ".join([self.p_names[p1]] + [self.d_names[self.best_tour[t]] for t in range(t1, t2)])

        tl, pl = trajectory[-1]
        res_str[-1] = " ".join([self.p_names[pl]] + [self.d_names[self.best_tour[t]] for t in range(tl, self.L)])

        for s in res_str:
            print(s)


def read_input():
    kk, ll = map(int, input().split())
    Solver.K, Solver.L = kk, ll

    Solver.update_dim()

    for ii in range(kk):
        # d_l, t^l_stay, r_l
        p, t1, t2 = input().split()
        Solver.p_names[ii] = p
        Solver.t_on[ii] = int(float(t1) * 1000)
        Solver.t_off[ii] = int(float(t2) * 1000)

    for ii in range(ll):
        # d_l, t^l_stay, r_l
        d, t, r = input().split()
        Solver.d_names[ii] = d
        Solver.t_stay[ii] = int(float(t) * 1000)
        Solver.r_by[ii] = int(r) * 1000
    Solver.r_by[Solver.r_by == 0] = 10000000

    # a_{k1, k2}
    for ii in range(kk):
        Solver.a_mat[ii, :] = 4 * np.array(list(map(int, input().split())), dtype=np.int32)
    Solver.a_mat[Solver.a_mat < 0] = LARGE

    # b_{l1, l2}
    for ii in range(ll):
        bc = 10 * np.array(list(map(int, input().split())), dtype=np.int32)
        Solver.b_mat[ii, :] = bc[:kk]
        Solver.c_mat[ii, :] = bc[kk:]


if __name__ == "__main__":

    read_input()
    np.random.seed(57)
    sol = Solver(initial_tour=np.arange(Solver.L))

    for t_iter in range(1, 10000000):
        i, j = np.random.choice(Solver.L, 2, replace=False)
        i, j = min(i, j), max(i, j)
        if i > 0:
            tour_new = np.concatenate([sol.tour[:i], sol.tour[j:i - 1:-1], sol.tour[j + 1:]], axis=0)
        else:
            tour_new = np.concatenate([sol.tour[j::-1], sol.tour[j + 1:]], axis=0)

        new_score = sol.score_tour(tour_new)
        if new_score > sol.best_score:
            sol.update_tour(tour_new, new_score)

        if time_stamper() - t_zero > 58.5:
            break

    sol.print_best_tour()
