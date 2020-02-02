import numpy as np

# t -> 1000t
LARGE = 240 * 1000 + 1


class Data:

    def __init__(self, k, l):
        self.K = k
        self.L = l

        self.t_on = np.zeros(k, dtype=np.int32)
        self.t_off = np.zeros(k, dtype=np.int32)
        self.p_names = [""] * k

        self.t_stay = np.zeros(l, dtype=np.int32)
        self.r_by = np.zeros(l, dtype=np.int32)
        self.d_names = [""] * l

        self.a_mat = np.zeros((k, k), dtype=np.int32)
        self.b_mat = np.zeros((l, k), dtype=np.int32)
        self.c_mat = np.zeros((l, l), dtype=np.int32)
        self.d_mat = np.zeros((l, l), dtype=np.int32)

    def pseudo_d(self):
        for i1 in range(self.L):
            for i2 in range(self.L):
                dd = self.a_mat.copy()
                dd += self.b_mat[i2, :] + self.t_off
                dd += (self.b_mat[i1, :] + self.t_on)[:, np.newaxis]
                self.d_mat[i1, i2] = dd.min()
        self.d_mat = np.minimum(self.d_mat, self.c_mat)
        self.d_mat += self.t_stay
        return None

    def pseudo_score(self, tour, t_120=120000, t_240=240000):
        score = 10000
        time = 0
        time += (self.b_mat[tour[0], :] + self.t_off).min()
        time += self.t_stay[tour[0]]
        # skip validity(initial)
        for i in range(1, self.L):
            time += self.d_mat[tour[i - 1], tour[i]]
            if self.r_by[tour[i]] == 240 * 1000:
                if time > t_240:
                    score -= 100000 + (time - t_240)
                else:
                    score += 10000
            elif self.r_by[tour[i]] == 120 * 1000:
                if time > t_120:
                    score -= 100000 + (time - t_120)
                else:
                    score += 10000
            else:
                if time <= t_240:
                    score += 10000

        return score, time


def read_input():
    k, l = map(int, input().split())
    data = Data(k, l)

    for i in range(k):
        # d_l, t^l_stay, r_l
        p, t1, t2 = input().split()
        data.p_names[i] = p
        data.t_on[i] = int(float(t1) * 1000)
        data.t_off[i] = int(float(t2) * 1000)

    for i in range(l):
        # d_l, t^l_stay, r_l
        d, t, r = input().split()
        data.d_names[i] = d
        data.t_stay[i] = int(float(t) * 1000)
        data.r_by[i] = int(r) * 1000

    # a_{k1, k2}
    for i in range(k):
        data.a_mat[i, :] = 4 * np.array(list(map(int, input().split())), dtype=np.int32)
    data.a_mat[data.a_mat < 0] = LARGE

    # b_{l1, l2}
    for i in range(l):
        bc = 10 * np.array(list(map(int, input().split())), dtype=np.int32)
        data.b_mat[i, :] = bc[:k]
        data.c_mat[i, :] = bc[k:]

    data.pseudo_d()

    return data


class CarFitter:

    def __init__(self, data):
        self.data = data

    def fit_car(self, tour):

        dp = np.ones((self.data.K, 10), dtype=np.int32) * LARGE
        # initialize
        dp[:, 0] = self.data.t_off + self.data.b_mat[tour[0], :]
        dp_arr_from = -1 * np.ones((self.data.K, self.data.L), dtype=np.int32)
        dp_arr_when = -1 * np.ones((self.data.K, self.data.L), dtype=np.int32)

        res = self.data.t_stay[tour[0]]

        # update
        for j in range(1, self.data.L):
            j_ = j % 10

            when_v = dp.argmin(axis=1)
            # distance + to
            dist_m = self.data.a_mat + self.data.b_mat[tour[j], :] + self.data.t_off
            # from
            dist_m += (dp.min(axis=1) + self.data.b_mat[tour[j - 1], :] + self.data.t_on)[:, np.newaxis]
            dist_m -= self.data.c_mat[tour[j - 1], tour[j]]

            dp[:, j_] = dist_m.min(axis=0)
            dp_arr_from[:, j] = dist_m.argmin(axis=0)
            dp_arr_when[:, j] = when_v[dp_arr_from[:, j]]

            res += self.data.c_mat[tour[j - 1], tour[j]]
            res += self.data.t_stay[tour[j]]

        # trajectory from reverse direction
        trajectory = []
        arg_m = dp.argmin()
        tp_, tf = arg_m % 10, arg_m // 10
        tp = self.data.L
        tp -= ((tp - tp_ - 1) % 10 + 1)
        trajectory.append([tp, tf])
        while tp > 0:
            tp_, tf = dp_arr_when[tf, tp], dp_arr_from[tf, tp]
            tp -= ((tp - tp_ - 1) % 10 + 1)
            trajectory.append([tp, tf])

        return list(reversed(trajectory))

    def score_tour(self, tour, car_tour):

        score = 0
        time = 0
        valid_120 = True
        valid_240 = True
        valid_path = True
        valid_10 = True

        for i in range(len(car_tour) - 1):
            t1, p1 = car_tour[i]
            t2, p2 = car_tour[i + 1]
            if t2 - t1 > 10:
                valid_10 = False
            time += self.data.t_off[p1]
            time += self.data.b_mat[tour[t1], p1]
            for t in range(t1, t2):
                time += self.data.t_stay[tour[t]]
                # validity
                if self.data.r_by[tour[t]] > 0:
                    if time > self.data.r_by[tour[t]]:
                        if self.data.r_by[tour[t]] == 240 * 1000:
                            valid_240 = False
                        else:
                            valid_120 = False
                    else:
                        score += 10000
                else:
                    if time <= 240000:
                        score += 10000
                if t + 1 < t2:
                    time += self.data.c_mat[tour[t], tour[t + 1]]
            time += self.data.b_mat[tour[t2 - 1], p1]
            time += self.data.t_on[p1]
            time += self.data.a_mat[p1, p2]
            if self.data.a_mat[p1, p2] == LARGE:
                valid_path = False

        # last
        tl, pl = car_tour[-1]
        if self.data.L - tl > 10:
            valid_10 = False
        time += self.data.t_off[pl]
        time += self.data.b_mat[tour[tl], pl]
        for t in range(tl, self.data.L):
            time += self.data.t_stay[tour[t]]
            # validity
            if self.data.r_by[tour[t]] > 0:
                if time > self.data.r_by[tour[t]]:
                    if self.data.r_by[tour[t]] == 240 * 1000:
                        valid_240 = False
                    else:
                        valid_120 = False
                else:
                    score += 10000
            else:
                if time <= 240000:
                    score += 10000
            if t + 1 < self.data.L:
                time += self.data.c_mat[tour[t], tour[t + 1]]

        if time < 240000:
            score += int((240000 - time) * 60 / 1000)
        if valid_120 and valid_240 and valid_10 and valid_path:
            return score, (valid_120, valid_240)
        else:
            return 0, (valid_120, valid_240)

    def print_tour(self, tour, car_tour):

        res_str = [""] * len(car_tour)

        for i in range(len(car_tour) - 1):
            t1, p1 = car_tour[i]
            t2, p2 = car_tour[i + 1]
            res_str[i] = " ".join([self.data.p_names[p1]] + [self.data.d_names[tour[t]] for t in range(t1, t2)])

        tl, pl = car_tour[-1]
        res_str[-1] = " ".join([self.data.p_names[pl]] + [self.data.d_names[tour[t]] for t in range(tl, self.data.L)])

        for s in res_str:
            print(s)


if __name__ == "__main__":

    np.random.seed(57)

    dat = read_input()
    cf = CarFitter(dat)
    tour = np.arange(dat.L).astype(np.int32)
    res_car = cf.fit_car(tour)
    # print(cf.score_tour(tour, res_car))
    t_120 = 80000
    t_240 = 160000
    score_now, time_now = dat.pseudo_score(tour, t_120=t_120, t_240=t_240)
    for _ in range(10000):
        i, j = np.random.choice(dat.L, 2, replace=False)
        i, j = min(i, j), max(i, j)
        if i > 0:
            tour_new = np.concatenate([tour[:i], tour[j:i - 1:-1], tour[j + 1:]], axis=0)
        else:
            tour_new = np.concatenate([tour[j::-1], tour[j + 1:]], axis=0)
        score, time = dat.pseudo_score(tour_new, t_120=t_120, t_240=t_240)
        if score > score_now or (score == score_now and time < time_now):
            tour = tour_new
            score_now = score
            time_now = time

    res_car = cf.fit_car(tour)
    score_1, valid_1 = cf.score_tour(tour, res_car)

    # 2nd stage
    for _ in range(5000):
        i, j = np.random.choice(dat.L, 2, replace=False)
        i, j = min(i, j), max(i, j)
        if i > 0:
            tour_new = np.concatenate([tour[:i], tour[j:i - 1:-1], tour[j + 1:]], axis=0)
        else:
            tour_new = np.concatenate([tour[j::-1], tour[j + 1:]], axis=0)
        res_car_new = cf.fit_car(tour_new)
        score_1_new, _ = cf.score_tour(tour_new, res_car_new)
        if score_1_new > score_1:
            tour = tour_new
            score_1 = score_1_new
            res_car = res_car_new

    cf.print_tour(tour, res_car)
