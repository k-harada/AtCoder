def solve(n, ab_list):
    res = 0
    aoki = 0
    takahashi = 0
    for a, b in ab_list:
        aoki += a
    ab_list_s = sorted(ab_list, key=lambda x: x[1] + 2 * x[0], reverse=True)
    # print(ab_list_s)
    for a, b in ab_list_s:
        aoki -= a
        takahashi += a + b
        res += 1
        if takahashi > aoki:
            return res
    return 0


def main():
    n = int(input())
    ab_list = [tuple(map(int, input().split())) for _ in range(n)]
    res = solve(n, ab_list)
    print(res)


def test():
    assert solve(4, [(2, 1), (2, 2), (5, 1), (1, 3)]) == 1
    assert solve(5, [(2, 1), (2, 1), (2, 1), (2, 1), (2, 1)]) == 3
    assert solve(1, [(273, 691)]) == 1


if __name__ == "__main__":
    test()
    main()
