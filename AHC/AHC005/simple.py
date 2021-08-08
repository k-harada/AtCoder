from collections import deque
import random
import math
import time


class Solver:

    def __init__(self, n, s_i, s_j, c):

        # vertices
        vertices_list = [(s_i, s_j)]
        vertices_map = [[-1] * n for _ in range(n)]
        n_v = 1
        for i in range(n):
            for j in range(n):
                if c[i][j] == '#':
                    continue
                flag_1 = 0
                flag_2 = 0
                if i > 0:
                    if c[i - 1][j] != '#':
                        flag_1 = 1
                if i < n - 1:
                    if c[i + 1][j] != '#':
                        flag_1 = 1
                if j > 0:
                    if c[i][j - 1] != '#':
                        flag_2 = 1
                if j < n - 1:
                    if c[i][j + 1] != '#':
                        flag_2 = 1

                if flag_1 * flag_2:
                    vertices_list.append((i, j))
                    vertices_map[i][j] = n_v
                    n_v += 1
        # edges
        edges_list = [[] for _ in range(n_v)]
        n_edge = 0

        for i in range(n):
            length = 0
            j0 = 0
            for j in range(n):
                if c[i][j] != '#':
                    if length == 0:
                        j0 = j
                    length += 1
                else:  # c[i][j] == '#'
                    if length > 1:
                        for k in range(j0, j):
                            if i == s_i and k == s_j:
                                edges_list[0].append(n_edge)
                            if vertices_map[i][k] >= 0:
                                edges_list[vertices_map[i][k]].append(n_edge)
                        n_edge += 1
                    length = 0
            # last
            if length > 1:
                for k in range(j0, n):
                    if i == s_i and k == s_j:
                        edges_list[0].append(n_edge)
                    if vertices_map[i][k] >= 0:
                        edges_list[vertices_map[i][k]].append(n_edge)
                n_edge += 1

        for j in range(n):
            length = 0
            i0 = 0
            for i in range(n):
                if c[i][j] != '#':
                    if length == 0:
                        i0 = i
                    length += 1
                else:  # c[i][j] == '#'
                    if length > 1:
                        for k in range(i0, i):
                            if k == s_i and j == s_j:
                                edges_list[0].append(n_edge)
                            if vertices_map[k][j] >= 0:
                                edges_list[vertices_map[k][j]].append(n_edge)
                        n_edge += 1
                    length = 0
            # last
            if length > 1:
                for k in range(i0, n):
                    if k == s_i and j == s_j:
                        edges_list[0].append(n_edge)
                    if vertices_map[k][j] >= 0:
                        edges_list[vertices_map[k][j]].append(n_edge)
                n_edge += 1
        # print(n_v, n_edge)
        # print(vertices_map)
        # print(edges_list)

        # distance between vertices
        distance_mat = [[10 * n * n] * n_v for _ in range(n_v)]
        move_mat = [[""] * n_v for _ in range(n_v)]
        cost_mat = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if c[i][j] == '#':
                    cost_mat[i][j] = 10000000
                else:
                    cost_mat[i][j] = int(c[i][j])

        for i in range(n_v):
            distance_temp = [[10 * n * n] * n for _ in range(n)]
            x0, y0 = vertices_list[i]
            distance_temp[x0][y0] = 0
            move_temp = [[""] * n for _ in range(n)]
            queue = deque([(x0, y0, "")])
            while len(queue):
                px, py, ps = queue.popleft()
                if px > 0:
                    qx, qy, qs = px - 1, py, ps + "U"
                    if distance_temp[px][py] + cost_mat[qx][qy] < distance_temp[qx][qy]:
                        distance_temp[qx][qy] = distance_temp[px][py] + cost_mat[qx][qy]
                        queue.append((qx, qy, qs))
                        move_temp[qx][qy] = qs
                if px < n - 1:
                    qx, qy, qs = px + 1, py, ps + "D"
                    if distance_temp[px][py] + cost_mat[qx][qy] < distance_temp[qx][qy]:
                        distance_temp[qx][qy] = distance_temp[px][py] + cost_mat[qx][qy]
                        queue.append((qx, qy, qs))
                        move_temp[qx][qy] = qs
                if py > 0:
                    qx, qy, qs = px, py - 1, ps + "L"
                    if distance_temp[px][py] + cost_mat[qx][qy] < distance_temp[qx][qy]:
                        distance_temp[qx][qy] = distance_temp[px][py] + cost_mat[qx][qy]
                        queue.append((qx, qy, qs))
                        move_temp[qx][qy] = qs
                if py < n - 1:
                    qx, qy, qs = px, py + 1, ps + "R"
                    if distance_temp[px][py] + cost_mat[qx][qy] < distance_temp[qx][qy]:
                        distance_temp[qx][qy] = distance_temp[px][py] + cost_mat[qx][qy]
                        queue.append((qx, qy, qs))
                        move_temp[qx][qy] = qs
            # get result
            for j in range(n_v):
                rx, ry = vertices_list[j]
                distance_mat[i][j] = distance_temp[rx][ry]
                move_mat[i][j] = move_temp[rx][ry]
        # print(distance_mat[1])

        self.n_v = n_v
        self.n_edge = n_edge
        self.edges_list = edges_list
        self.distance_mat = distance_mat
        self.move_mat = move_mat
        self.vertices_list = vertices_list

    def eval_path(self, path):
        flag = [0] * self.n_edge
        cost = 0
        for e in self.edges_list[0]:
            flag[e] = 1
        st = 0
        for i in range(1, self.n_v + 1):
            if min([flag[e] for e in self.edges_list[path[i]]]) == 1 and i < self.n_v:
                continue
            else:
                for e in self.edges_list[path[i]]:
                    flag[e] = 1
                cost += self.distance_mat[path[st]][path[i]]
                st = i
        return cost

    def return_path(self, path):
        flag = [0] * self.n_edge
        res_path = ""
        for e in self.edges_list[0]:
            flag[e] = 1
        st = 0
        for i in range(1, self.n_v + 1):
            if min([flag[e] for e in self.edges_list[path[i]]]) == 1 and i < self.n_v:
                continue
            else:
                for e in self.edges_list[path[i]]:
                    flag[e] = 1
                res_path += self.move_mat[path[st]][path[i]]
                # print(self.move_mat[path[st]][path[i]], self.distance_mat[path[st]][path[i]])
                st = i
        return res_path


def solve(n, s_i, s_j, c):
    t0 = time.time()
    sol = Solver(n, s_i, s_j, c)
    path = list(range(sol.n_v)) + [0]
    dist_mat = sol.distance_mat
    score_base = sol.eval_path(path)
    best_path = path.copy()

    # simple TSP
    for n1 in range(10000000):
        t = time.time() - t0
        if t > 1.5:
            break
        temperature = 10 / (t + 0.01)
        i0 = random.choice(range(1, sol.n_v + 1))
        j0 = random.choice(range(1, sol.n_v + 1))
        i0, j0 = min(i0, j0), max(i0, j0)
        d_base = dist_mat[path[i0 - 1]][path[i0]] + dist_mat[path[j0 - 1]][path[j0]]
        d_new = dist_mat[path[i0 - 1]][path[j0 - 1]] + dist_mat[path[i0]][path[j0]]
        score_diff = d_base - d_new
        if score_diff >= 0 or math.exp(score_diff / temperature) > random.uniform(0.0, 1.0):
            path = path[:i0] + list(reversed(path[i0:j0])) + path[j0:]
        else:
            pass

    for n2 in range(1000000):
        t = time.time() - t0
        if t > 2.75:
            break
        i0 = random.choice(range(1, sol.n_v + 1))
        j0 = random.choice(range(1, sol.n_v + 1))
        i0, j0 = min(i0, j0), max(i0, j0)
        path = path[:i0] + list(reversed(path[i0:j0])) + path[j0:]
        score = sol.eval_path(path)
        score_diff = score_base - score
        if score_diff >= 0:
            score_base = score
        else:
            # undo
            path = path[:i0] + list(reversed(path[i0:j0])) + path[j0:]
    res = sol.return_path(path)
    # print(n1, n2)
    # print(path)
    # print(score_base)
    return res


def main():
    n, s_i, s_j = map(int, input().split())
    c = [input() for _ in range(n)]
    res = solve(n, s_i, s_j, c)
    print(res)


if __name__ == "__main__":
    main()
