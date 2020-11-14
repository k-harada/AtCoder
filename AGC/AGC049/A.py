from collections import deque


def solve(n, s_list):

    reach_mat = [[0] * n for _ in range(n)]
    for i in range(n):
        reach_mat[i][i] = 1
        queue = deque([i])
        while len(queue) > 0:
            p = queue.popleft()
            for q in range(n):
                if reach_mat[i][q] == 1:
                    continue
                if s_list[p][q] == '1':
                    reach_mat[i][q] = 1
                    queue.append(q)

    # print(reach_mat)

    res = 0.0
    active = [1] * n

    for i in range(n):
        if active[i] == 0:
            continue
        same = 0
        parent = 0
        for j in range(n):
            if reach_mat[i][j] == 0 and reach_mat[j][i] == 1:
                parent += 1
            elif reach_mat[i][j] == 1 and reach_mat[j][i] == 1:
                same += 1
        res += same / (same + parent)
        for j in range(n):
            if reach_mat[i][j] == 1 and reach_mat[j][i] == 1:
                active[j] = 0
    return res


def main():
    n = int(input())
    s_list = [input() for _ in range(n)]
    res = solve(n, s_list)
    print(res)


def test():
    assert abs(solve(3, ['010', '001', '010']) - 1.6666666666) < 10 ** (-9)
    assert abs(solve(3, ['000', '000', '000']) - 3.0) < 10 ** (-9)
    assert abs(solve(3, ['011', '101', '110']) - 1.0) < 10 ** (-9)


if __name__ == "__main__":
    test()
    main()
