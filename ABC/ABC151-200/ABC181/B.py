def solve(n, ab_list):
    res = 0
    for a, b in ab_list:
        res += (b + a) * (b - a + 1) // 2
    return res


def main():
    n = int(input())
    ab_list = [tuple(map(int, input().split())) for _ in range(n)]
    res = solve(n, ab_list)
    print(res)


def test():
    assert solve(2, [(1, 3), (3, 5)]) == 18
    assert solve(3, [(11, 13), (17, 47), (359, 44683)]) == 998244353
    assert solve(1, [(1, 1000000)]) == 500000500000


if __name__ == "__main__":
    test()
    main()
