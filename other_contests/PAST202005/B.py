def solve(n, m, q, s_list):
    solved = [[0] * m for _ in range(n)]
    score_list = [n] * m
    res_list = []
    for s in s_list:
        if s[0] == 1:
            i = s[1] - 1
            res = 0
            for j in range(m):
                res += score_list[j] * solved[i][j]
            res_list.append(res)
        else:
            i, j = s[1] - 1, s[2] - 1
            score_list[j] -= 1
            solved[i][j] = 1
    return res_list


def main():
    n, m, q = map(int, input().split())
    s_list = [list(map(int, input().split())) for _ in range(q)]
    res = solve(n, m, q, s_list)
    for r in res:
        print(r)


def test():
    assert solve(2, 1, 6, [[2, 1, 1], [1, 1], [1, 2], [2, 2, 1], [1, 1], [1, 2]]) == [1, 0, 0, 0]


if __name__ == "__main__":
    test()
    main()
