def solve(n, m, ab_list):
    target_list = []
    for a, b in ab_list:
        target_list.append(f"{a} {b}")
        c = a + 2
        d = b + 1
        if 1 <= c <= n and 1 <= d <= n:
            target_list.append(f"{c} {d}")
        c = a + 1
        d = b + 2
        if 1 <= c <= n and 1 <= d <= n:
            target_list.append(f"{c} {d}")
        c = a - 1
        d = b + 2
        if 1 <= c <= n and 1 <= d <= n:
            target_list.append(f"{c} {d}")
        c = a - 2
        d = b + 1
        if 1 <= c <= n and 1 <= d <= n:
            target_list.append(f"{c} {d}")
        c = a - 2
        d = b - 1
        if 1 <= c <= n and 1 <= d <= n:
            target_list.append(f"{c} {d}")
        c = a - 1
        d = b - 2
        if 1 <= c <= n and 1 <= d <= n:
            target_list.append(f"{c} {d}")
        c = a + 1
        d = b - 2
        if 1 <= c <= n and 1 <= d <= n:
            target_list.append(f"{c} {d}")
        c = a + 2
        d = b - 1
        if 1 <= c <= n and 1 <= d <= n:
            target_list.append(f"{c} {d}")
    res = n * n - len(set(target_list))
    return res


def main():
    n, m = map(int, input().split())
    ab_list = [tuple(map(int, input().split())) for _ in range(m)]
    res = solve(n, m, ab_list)
    print(res)


def test():
    assert solve(8, 6, [
        (1, 4), (2, 1), (3, 8), (4, 5), (5, 2), (8, 3)
    ]) == 38
    assert solve(1000000000, 1, [(1, 1)]) == 999999999999999997
    assert solve(20, 10, [
        (1, 4),
        (7, 11),
        (7, 15),
        (8, 10),
        (11, 6),
        (12, 5),
        (13, 1),
        (15, 2),
        (20, 10),
        (20, 15),
    ]) == 338


if __name__ == "__main__":
    test()
    main()
