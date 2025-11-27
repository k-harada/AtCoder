def solve(n, x, ab_list):
    res_min = []
    t_now = 0
    c = 0
    b_cum_min = ab_list[0][1]
    for a, b in ab_list:
        t_now += a + b
        c += 1
        b_cum_min = min(b_cum_min, b)
        r = t_now + (x - c) * b_cum_min
        res_min.append(r)
        if c == x:
            break
    return min(res_min)


def main():
    n, x = map(int, input().split())
    ab_list = [tuple(map(int, input().split())) for _ in range(n)]
    res = solve(n, x, ab_list)
    print(res)


def test():
    assert solve(3, 4, [(3, 4), (2, 3), (4, 2)]) == 18
    assert solve(10, 1000000000, [
        (3, 3), (1, 6), (4, 7), (1, 8), (5, 7),
        (9, 9), (2, 4), (6, 4), (5, 1), (3, 1)
    ]) == 1000000076


if __name__ == "__main__":
    test()
    main()
