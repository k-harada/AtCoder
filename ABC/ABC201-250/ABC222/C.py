def rcp(x, y):
    if x == y:
        return 0
    elif x == "G" and y == "C":
        return 1
    elif x == "C" and y == "P":
        return 1
    elif x == "P" and y == "G":
        return 1
    else:
        return -1


def solve(n, m, a_list):
    res = [0] * (2 * n)
    for i in range(m):
        res_s = list(sorted(list(zip(res, list(range(2 * n)))), key=lambda x: (-x[0], x[1])))
        for j in range(n):
            p = res_s[2 * j][1]
            q = res_s[2 * j + 1][1]
            res_p = rcp(a_list[p][i], a_list[q][i])
            if res_p == 1:
                res[p] += 1
            elif res_p == -1:
                res[q] += 1
    res_s = list(sorted(list(zip(res, list(range(2 * n)))), key=lambda x: (-x[0], x[1])))
    # print(res_s)
    return [res_s[i][1] + 1 for i in range(2 * n)]


def main():
    n, m = map(int, input().split())
    a_list = [input() for _ in range(2 * n)]
    res = solve(n, m, a_list)
    for r in res:
        print(r)


def test():
    assert solve(2, 3, ["GCP", "PPP", "CCC", "PPC"]) == [3, 1, 2, 4]
    assert solve(2, 2, ["GC", "PG", "CG", "PP"]) == [1, 2, 3, 4]


if __name__ == "__main__":
    test()
    main()
