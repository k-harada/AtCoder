from itertools import combinations


def solve(n, t, m, ab_list):
    pattern_list = []
    for c in combinations(list(range(n)), t):
        d = []
        for i in range(n):
            if i not in c:
                d.append(i)
        # print(c, d)
        for k in range(t ** (n - t)):
            flag = True
            x = [-1] * n
            for j, p in enumerate(c):
                x[p] = j
            for j, q in enumerate(d):
                r = (k // (t ** j)) % t
                if c[r] > q:
                    flag = False
                x[q] = r
            if flag:
                pattern_list.append("".join([str(a) for a in x]))
    # print(len(pattern_list))
    # print(len(set(pattern_list)))
    res = 0
    for p in pattern_list:
        r = 1
        for a, b in ab_list:
            if p[a - 1] == p[b - 1]:
                r = 0
        res += r
    return res


def main():
    n, t, m = map(int, input().split())
    ab_list = [tuple(map(int, input().split())) for _ in range(m)]
    res = solve(n, t, m, ab_list)
    print(res)
    # for r in res:
    #     print(r)


def test():
    assert solve(5, 2, 2, [(1, 3), (3, 4)]) == 4
    assert solve(5, 1, 2, [(1, 3), (3, 4)]) == 0
    assert solve(6, 4, 0, []) == 65
    assert solve(10, 6, 8, [
        (5, 9),
        (1, 4),
        (3, 8),
        (1, 6),
        (4, 10),
        (5, 7),
        (5, 6),
        (3, 7),
    ]) == 8001


if __name__ == "__main__":
    test()
    main()
