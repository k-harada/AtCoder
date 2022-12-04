from bisect import bisect_left, bisect_right


def solve(n, q, s, lr_list):

    switch_forward = [0] * (n + 1)
    switch = 0
    for i in range(1, n):
        if s[i] != s[i - 1]:
            switch += 1

        switch_forward[i + 1] = switch

    res = []
    for le, ri in lr_list:

        c = switch_forward[ri] - switch_forward[le]
        if s[le - 1] != s[ri - 1]:
            c += 1

        res.append((c + 1) // 2)
    # print(res)
    return res


def main():
    n, q = map(int, input().split())
    s = input()
    lr_list = [tuple(map(int, input().split())) for _ in range(q)]
    res = solve(n, q, s, lr_list)
    for r in res:
        print(r)


def test():
    assert solve(6, 4, "ABCCCA", [(3, 5), (2, 3), (1, 3), (1, 6)]) == [0, 1, 2, 2]


if __name__ == "__main__":
    test()
    main()
