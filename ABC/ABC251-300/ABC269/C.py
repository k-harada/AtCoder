from itertools import combinations


def solve(n):
    i_list = []
    for i in range(60):
        if (n >> i) & 1:
            i_list.append(i)
    res = [0]
    m = len(i_list)
    for r in range(1, m + 1):
        for p in combinations(i_list, r):
            x = 0
            for q in p:
                x += 2 ** q
            res.append(x)
    res = list(sorted(res))
    return res


def main():
    n = int(input())
    res = solve(n)
    for r in res:
        print(r)


def test():
    assert solve(11) == [0, 1, 2, 3, 8, 9, 10, 11]
    assert solve(0) == [0]
    assert solve(576461302059761664) == [
        0, 524288, 549755813888, 549756338176, 576460752303423488,
        576460752303947776, 576461302059237376, 576461302059761664
    ]


def test_large():
    print(solve(2 ** 16 - 1))


if __name__ == "__main__":
    test()
    # test_large()
    main()
