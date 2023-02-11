def solve(s_x, s_y, t_x, t_y, a, b, c, d):
    if (s_x - t_x) % 2 == 1 or (s_y - t_y) % 2 == 1:
        return ["No"]
    dx = b - a
    dy = d - c
    res = ["Yes"]
    if (dx == 0 and s_x != t_x) or (dy == 0 and s_y != t_y):
        res.append(f"{a} {c}")
        s_x = 2 * a - s_x
        s_y = 2 * c - s_y
    if (dx == 0 and s_x != t_x) or (dy == 0 and s_y != t_y):
        return ["No"]

    if s_x < t_x:
        n_x = (t_x - s_x) // (2 * dx)
        for _ in range(n_x):
            res.append(f"{a} {c}")
            res.append(f"{b} {c}")
        s_x += n_x * 2 * dx
    elif s_x > t_x:
        n_x = (s_x - t_x) // (2 * dx)
        for _ in range(n_x):
            res.append(f"{b} {c}")
            res.append(f"{a} {c}")
        s_x -= n_x * 2 * dx
    if s_x < t_x:
        res.append(f"{a} {c}")
        x = a + (t_x - s_x) // 2
        res.append(f"{x} {c}")
    elif s_x > t_x:
        res.append(f"{b} {c}")
        x = b + (t_x - s_x) // 2
        res.append(f"{x} {c}")

    if s_y < t_y:
        n_y = (t_y - s_y) // (2 * dy)
        for _ in range(n_y):
            res.append(f"{a} {c}")
            res.append(f"{a} {d}")
        s_y += n_y * 2 * dy
    elif s_y > t_y:
        n_y = (s_y - t_y) // (2 * dy)
        for _ in range(n_y):
            res.append(f"{a} {d}")
            res.append(f"{a} {c}")
        s_y -= n_y * 2 * dy
    if s_y < t_y:
        res.append(f"{a} {c}")
        y = c + (t_y - s_y) // 2
        res.append(f"{a} {y}")
    elif s_y > t_y:
        res.append(f"{a} {d}")
        y = d + (t_y - s_y) // 2
        res.append(f"{a} {y}")

    return res


def main():
    s_x, s_y = map(int, input().split())
    t_x, t_y = map(int, input().split())
    a, b, c, d = map(int, input().split())
    res = solve(s_x, s_y, t_x, t_y, a, b, c, d)
    for r in res:
        print(r)


def test():
    print(solve(1, 2, 7, 8, 7, 9, 0, 3))
    print(solve(0, 0, 8, 4, 5, 5, 0, 0))
    print(solve(1, 4, 1, 4, 100, 200, 300, 400))
    print(solve(22, 2, 16, 7, 14, 30, 11, 14))


if __name__ == "__main__":
    # test()
    main()
