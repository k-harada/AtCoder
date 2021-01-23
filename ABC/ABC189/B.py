def solve(n, x, vp_list):
    res = 0
    total = 0
    for v, p in vp_list:
        total += v * p
        res += 1
        if total > x * 100:
            return res
    return -1


def main():
    n, x = map(int, input().split())
    vp_list = [tuple(map(int, input().split())) for _ in range(n)]
    res = solve(n, x, vp_list)
    print(res)


def test():
    assert solve(2, 15, [(200, 5), (350, 3)]) == 2
    assert solve(2, 10, [(200, 5), (350, 3)]) == 2
    assert solve(3, 1000000, [(1000, 100), (1000, 100), (1000, 100)]) == -1


if __name__ == "__main__":
    test()
    main()
