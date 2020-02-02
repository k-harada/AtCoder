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
    d_mat = np.zeros((L, L), dtype=np.int32)
    d_ini = np.zeros(L, dtype=np.int32)

    def __init__(self, time_120, time_240):

        self.tour = np.arange(self.L)
        self.pseudo_time = np.zeros(self.L, dtype=np.int32)
        self.pseudo_dist = np.zeros(self.L, dtype=np.int32)
        self.pseudo_dist_rev = np.zeros(self.L, dtype=np.int32)
        self.pseudo_dist_try = np.zeros(self.L, dtype=np.int32)
        self.r_by_tour = np.zeros(self.L, dtype=np.int32)
        self.r_by_tour_try = np.zeros(self.L, dtype=np.int32)

        self.trajectory = []

        self.real_time = np.zeros(self.L, dtype=np.int32)

        self.time_120 = time_120
        self.time_240 = time_240

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
        cls.d_mat = np.zeros((cls.L, cls.L), dtype=np.int32)
        cls.d_ini = np.zeros(cls.L, dtype=np.int32)

    @classmethod
    def pseudo_d(cls):
        for i1 in range(cls.L):
            for i2 in range(cls.L):
                dd = cls.a_mat.copy()
                dd += cls.b_mat[i2, :] + cls.t_off
                dd += (cls.b_mat[i1, :] + cls.t_on)[:, np.newaxis]
                cls.d_mat[i1, i2] = dd.min()
        cls.d_mat = np.minimum(cls.d_mat, cls.c_mat)
        cls.d_mat += cls.t_stay
        cls.d_ini = (cls.b_mat + cls.t_off).min(axis=1) + cls.t_stay
        return None

    def pseudo_score_init(self, tour_init):

        self.tour = tour_init
        self.pseudo_dist[0] = self.d_ini[self.tour[0]]
        self.pseudo_dist_rev[-1] = self.d_ini[self.tour[-1]]

        for k in range(1, self.L):
            self.pseudo_dist[k] = self.d_mat[self.tour[k-1], self.tour[k]]
            self.pseudo_dist_rev[k-1] = self.d_mat[self.tour[k], self.tour[k-1]]

        # limit
        self.r_by_tour = self.r_by[self.tour]
        self.r_by_tour[self.r_by_tour == 0] = 100000000
        self.r_by_tour[self.r_by_tour == 120*1000] = self.time_120
        self.r_by_tour[self.r_by_tour == 240*1000] = self.time_240

        return pseudo_score(self.pseudo_dist, self.r_by_tour, self.time_240)

    def opt_2_pseudo_dry_run(self, i1, i2):

        if i1 > 0:
            self.pseudo_dist_try = np.concatenate([
                self.pseudo_dist[:i1], self.pseudo_dist_rev[i2:i1-1:-1], self.pseudo_dist[i2+1:]
            ], axis=0)
            self.pseudo_dist_try[i1] = self.d_mat[self.tour[i1-1], self.tour[i2]]
            if i2 + 1 < self.L:
                self.pseudo_dist_try[i2+1] = self.d_mat[self.tour[i1], self.tour[i2+1]]
            # r_by_tour_try
            self.r_by_tour_try = np.concatenate([
                self.r_by_tour[:i1], self.r_by_tour[i2:i1-1:-1], self.r_by_tour[i2+1:]
            ], axis=0)
        else:
            if i2 + 1 < self.L:
                self.pseudo_dist_try = np.concatenate([self.pseudo_dist_rev[i2::-1], self.pseudo_dist[i2+1:]], axis=0)
                self.pseudo_dist_try[0] = self.d_ini[self.tour[i2]]
                self.pseudo_dist_try[i2+1] = self.d_mat[self.tour[0], self.tour[i2+1]]
            else:
                self.pseudo_dist_try = self.pseudo_dist_rev[::-1]
            # r_by_tour_try
            self.r_by_tour_try = np.concatenate([self.r_by_tour[i2::-1], self.r_by_tour[i2+1:]], axis=0)

        return pseudo_score(self.pseudo_dist_try, self.r_by_tour_try, self.time_240)

    def opt_2_run(self, i1, i2):

        # r_by_tour
        self.r_by_tour = self.r_by_tour_try.copy()

        # tour
        if i1 > 0:
            self.tour = np.concatenate([self.tour[:i1], self.tour[i2:i1-1:-1], self.tour[i2+1:]], axis=0)
        else:
            self.tour = np.concatenate([self.tour[i2::-1], self.tour[i2+1:]], axis=0)

        # pseudo_dist_rev
        if i1 > 0:
            self.pseudo_dist_rev = np.concatenate([
                self.pseudo_dist_rev[:i1], self.pseudo_dist[i2:i1-1:-1], self.pseudo_dist_rev[i2+1:]
            ], axis=0)
            self.pseudo_dist_rev[i1-1] = self.d_mat[self.tour[i1], self.tour[i1-1]]
            if i2 + 1 < self.L:
                self.pseudo_dist_rev[i2] = self.d_mat[self.tour[i2+1], self.tour[i2]]
            else:
                self.pseudo_dist_rev[i2] = self.d_ini[self.tour[i2]]
        else:
            if i2 + 1 < self.L:
                self.pseudo_dist_rev = np.concatenate([self.pseudo_dist[i2::-1], self.pseudo_dist_rev[i2+1:]], axis=0)
                self.pseudo_dist_rev[i2] = self.d_mat[self.tour[i2+1], self.tour[i2]]
            else:
                self.pseudo_dist_rev = self.pseudo_dist[::-1]
        # pseudo_dist
        self.pseudo_dist = self.pseudo_dist_try.copy()

    def fit_car(self):

        dp = np.ones((self.K, 10), dtype=np.int32) * LARGE
        # initialize
        dp[:, 0] = self.t_off + self.b_mat[self.tour[0], :]
        dp_arr_from = -1 * np.ones((self.K, self.L), dtype=np.int32)
        dp_arr_when = -1 * np.ones((self.K, self.L), dtype=np.int32)

        res = self.t_stay[self.tour[0]]

        # update
        for jj in range(1, self.L):
            j_ = jj % 10

            when_v = dp.argmin(axis=1)
            # distance + to
            dist_m = self.a_mat + self.b_mat[self.tour[jj], :] + self.t_off
            # from
            dist_m += (dp.min(axis=1) + self.b_mat[self.tour[jj - 1], :] + self.t_on)[:, np.newaxis]
            dist_m -= self.c_mat[self.tour[jj - 1], self.tour[jj]]

            dp[:, j_] = dist_m.min(axis=0)
            dp_arr_from[:, jj] = dist_m.argmin(axis=0)
            dp_arr_when[:, jj] = when_v[dp_arr_from[:, jj]]

            res += self.c_mat[self.tour[jj - 1], self.tour[jj]]
            res += self.t_stay[self.tour[jj]]

        # trajectory from reverse direction
        self.trajectory = []
        arg_m = dp.argmin()
        tp_, tf = arg_m % 10, arg_m // 10
        tp = self.L
        tp -= ((tp - tp_ - 1) % 10 + 1)
        self.trajectory.append([tp, tf])
        while tp > 0:
            tp_, tf = dp_arr_when[tf, tp], dp_arr_from[tf, tp]
            tp -= ((tp - tp_ - 1) % 10 + 1)
            self.trajectory.append([tp, tf])

        self.trajectory = list(reversed(self.trajectory))

    def score_tour(self):

        real_score = 0
        time = 0
        valid_120 = True
        valid_240 = True
        valid_path = True
        valid_10 = True

        for ii in range(len(self.trajectory) - 1):
            t1, p1 = self.trajectory[ii]
            t2, p2 = self.trajectory[ii + 1]
            if t2 - t1 > 10:
                valid_10 = False
            time += self.t_off[p1]
            time += self.b_mat[self.tour[t1], p1]
            for t in range(t1, t2):
                time += self.t_stay[self.tour[t]]
                self.real_time[t] = time
                # validity
                if self.r_by[self.tour[t]] > 0:
                    if time > self.r_by[self.tour[t]]:
                        if self.r_by[self.tour[t]] == 240 * 1000:
                            valid_240 = False
                        else:
                            valid_120 = False
                    else:
                        real_score += 10000
                else:
                    if time <= 240000:
                        real_score += 10000
                if t + 1 < t2:
                    time += self.c_mat[self.tour[t], self.tour[t + 1]]
            time += self.b_mat[self.tour[t2 - 1], p1]
            time += self.t_on[p1]
            time += self.a_mat[p1, p2]
            if self.a_mat[p1, p2] == LARGE:
                valid_path = False

        # last
        tl, pl = self.trajectory[-1]
        if self.L - tl > 10:
            valid_10 = False
        time += self.t_off[pl]
        time += self.b_mat[self.tour[tl], pl]
        for t in range(tl, self.L):
            time += self.t_stay[self.tour[t]]
            self.real_time[t] = time
            # validity
            if self.r_by[self.tour[t]] > 0:
                if time > self.r_by[self.tour[t]]:
                    if self.r_by[self.tour[t]] == 240 * 1000:
                        valid_240 = False
                    else:
                        valid_120 = False
                else:
                    real_score += 10000
            else:
                if time <= 240000:
                    real_score += 10000
            if t + 1 < self.L:
                time += self.c_mat[self.tour[t], self.tour[t + 1]]

        if time < 240000:
            real_score += int((240000 - time) * 60 / 1000)
        if valid_120 and valid_240 and valid_10 and valid_path:
            return real_score, (valid_120, valid_240)
        else:
            return 0, (valid_120, valid_240)

    def print_tour(self):

        res_str = [""] * len(self.trajectory)

        for ii in range(len(self.trajectory) - 1):
            t1, p1 = self.trajectory[ii]
            t2, p2 = self.trajectory[ii + 1]
            res_str[ii] = " ".join([self.p_names[p1]] + [self.d_names[self.tour[t]] for t in range(t1, t2)])

        tl, pl = self.trajectory[-1]
        res_str[-1] = " ".join([self.p_names[pl]] + [self.d_names[self.tour[t]] for t in range(tl, self.L)])

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

    # a_{k1, k2}
    for ii in range(kk):
        Solver.a_mat[ii, :] = 4 * np.array(list(map(int, input().split())), dtype=np.int32)
    Solver.a_mat[Solver.a_mat < 0] = LARGE

    # b_{l1, l2}
    for ii in range(ll):
        bc = 10 * np.array(list(map(int, input().split())), dtype=np.int32)
        Solver.b_mat[ii, :] = bc[:kk]
        Solver.c_mat[ii, :] = bc[kk:]

    Solver.pseudo_d()


def pseudo_score(pseudo_dist, r_by_tour, time_240=240000):

    pseudo_time = np.cumsum(pseudo_dist)

    # base score
    s = 10000 * (pseudo_time <= time_240).sum()
    # late penalty
    v = np.maximum(pseudo_time - r_by_tour, 0)
    s -= 100000 * (v > 0).sum()
    s -= v.sum()
    # total time penalty
    s -= pseudo_time[-1] * 60 // 1000

    return s


if __name__ == "__main__":

    read_input()
    np.random.seed(57)
    sol_s = [
        Solver(120000, 240000), Solver(110000, 220000), Solver(100000, 200000),
        Solver(90000, 180000), Solver(80000, 160000)
    ]
    N = len(sol_s)
    score_now = [sol.pseudo_score_init(sol.tour) for sol in sol_s]

    for t_iter in range(1, 10000000):
        i, j = np.random.choice(Solver.L, 2, replace=False)
        i, j = min(i, j), max(i, j)
        for k in range(N):
            sol = sol_s[k]
            score = sol.opt_2_pseudo_dry_run(i, j)
            if score > score_now[k]:
                sol.opt_2_run(i, j)
                score_now[k] = score

        if time_stamper() - t_zero > 55.0:
            break

    score_vec = np.zeros(N, dtype=np.int32)
    for k in range(N):
        sol = sol_s[k]
        sol.fit_car()
        score_1, valid_1 = sol.score_tour()
        score_vec[k] = score_1

    sol = sol_s[np.argmax(score_vec)]
    sol.print_tour()
