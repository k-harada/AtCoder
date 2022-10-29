def solve(n, m, t, ab_list):
    last = 0
    res = n
    for i in range(m):
        a, b = ab_list[i]
        res -= a - last
        if res <= 0:
            return "No"
        res += b - a
        res = min(n, res)
        last = b
    if res <= t - last:
        return "No"
    return "Yes"


def main():
    n, m, t = map(int, input().split())
    ab_list = [tuple(map(int, input().split())) for _ in range(m)]
    res = solve(n, m, t, ab_list)
    print(res)


def test():
    assert solve(10, 2, 20, [(9, 11), (13, 17)]) == "Yes"
    assert solve(10, 2, 20, [(9, 11), (13, 16)]) == "No"
    assert solve(15, 3, 30, [(5, 8), (15, 17), (24, 27)]) == "Yes"
    assert solve(20, 1, 30, [(20, 29)]) == "No"
    assert solve(20, 1, 30, [(1, 10)]) == "No"


if __name__ == "__main__":
    test()
    main()
