from heapq import heappop, heappush
import numpy as np


class Solver:

    def __init__(self):
        self.alpha = np.ones((30, 30), dtype=np.float)
        self.beta = np.ones((30, 30), dtype=np.float)
        self.last_points = (0, 0, 0, 0)
        self.last_path = ""

    def query(self, s_i, s_j, t_i, t_j):
        self.last_points = (s_i, s_j, t_i, t_j)
        d_array_mean = self.alpha / (self.alpha + self.beta)
        d_array_var = (self.alpha * self.beta) / (self.alpha + self.beta) ** 2 / (self.alpha + self.beta + 1.0)
        d_array_std = np.sqrt(d_array_var)
        d_act = 1000 + 8000 * (d_array_mean - d_array_std)
        d_act = np.maximum(d_act, 1)
        # print(d_act)
        # path
        distance = 1000000000000 * np.ones((30, 30), dtype=np.float)
        distance[s_i, s_j] = 0
        queue = []
        heappush(queue, (0, s_i, s_j, ""))
        shortest = [[""] * 30 for _ in range(30)]
        while len(queue):
            d, p_i, p_j, path = heappop(queue)
            if p_i > 0:
                q_i = p_i - 1
                q_j = p_j
                new_d = d + d_act[p_i - 1, p_j]
                if new_d < distance[q_i, q_j]:
                    distance[q_i, q_j] = new_d
                    shortest[q_i][q_j] = path + "U"
                    heappush(queue, (new_d, q_i, q_j, path + "U"))
            if p_i < 29:
                q_i = p_i + 1
                q_j = p_j
                new_d = d + d_act[p_i, p_j]
                if new_d < distance[q_i, q_j]:
                    distance[q_i, q_j] = new_d
                    shortest[q_i][q_j] = path + "D"
                    heappush(queue, (new_d, q_i, q_j, path + "D"))
            if p_j > 0:
                q_j = p_j - 1
                q_i = p_i
                new_d = d + d_act[p_i, p_j - 1]
                if new_d < distance[q_i, q_j]:
                    distance[q_i, q_j] = new_d
                    shortest[q_i][q_j] = path + "L"
                    heappush(queue, (new_d, q_i, q_j, path + "L"))
            if p_j < 29:
                q_j = p_j + 1
                q_i = p_i
                new_d = d + d_act[p_i, p_j]
                if new_d < distance[q_i, q_j]:
                    distance[q_i, q_j] = new_d
                    shortest[q_i][q_j] = path + "R"
                    heappush(queue, (new_d, q_i, q_j, path + "R"))
        self.last_path = shortest[t_i][t_j]
        # print(distance[t_i, t_j])
        return self.last_path

    def update(self, d):
        pass

    def _update(self, d):
        d_array_mean = self.alpha / (self.alpha + self.beta)
        d_act = 1000 + 8000 * d_array_mean
        d_total = 0
        s_i, s_j, t_i, t_j = self.last_points
        x = s_i
        y = s_j
        for c in self.last_path:
            if c == "U":
                x -= 1
                d_total += d_act[x, y]
            elif c == "D":
                d_total += d_act[x, y]
                x += 1
            elif c == "L":
                y -= 1
                d_total += d_act[x, y]
            else:
                d_total += d_act[x, y]
                y += 1
        update = (d - d_total) / 8000 / len(self.last_path)
        alpha_add = (update + 1) / 2
        beta_add = 1 - alpha_add
        for c in self.last_path:
            if c == "U":
                x -= 1
                self.alpha[x, y] += alpha_add
                self.beta[x, y] += beta_add
            elif c == "D":
                self.alpha[x, y] += alpha_add
                self.beta[x, y] += beta_add
                x += 1
            elif c == "L":
                y -= 1
                self.alpha[x, y] += alpha_add
                self.beta[x, y] += beta_add
            else:
                self.alpha[x, y] += alpha_add
                self.beta[x, y] += beta_add
                y += 1


def main():
    k = 1000
    solver = Solver()
    for _ in range(k):
        s_i, s_j, t_i, t_j = map(int, input().split())
        res = solver.query(s_i, s_j, t_i, t_j)
        print(res)
        d = int(input())
        solver.update(d)


if __name__ == "__main__":
    main()
