def solve(b, c):
    if b > 0:
        if c >= 2:
            p_max = b + (c - 2) // 2
        else:
            p_max = b
        p_min = b - c // 2
        n_min = - b - (c - 1) // 2
        n_max = - b + (c - 1) // 2
        if p_min <= n_max:
            return p_max - n_min + 1
        else:
            return p_max - p_min + 1 + n_max - n_min + 1
    elif b < 0:
        p_max = - b + (c - 1) // 2
        p_min = - b - (c - 1) // 2
        n_min = b - c // 2
        if c >= 2:
            n_max = - b + (c - 2) // 2
        else:
            n_max = b
        if p_min <= n_max:
            return p_max - n_min + 1
        else:
            return p_max - p_min + 1 + n_max - n_min + 1
    else:
        n_min = - (c // 2)
        if c >= 2:
            p_max = (c - 2) // 2
        else:
            p_max = 0
        return p_max - n_min + 1


def main():
    b, c = map(int, input().split())
    res = solve(b, c)
    print(res)


def test():
    assert solve(11, 2) == 3
    assert solve(0, 4) == 4
    assert solve(112, 20210213) == 20210436
    assert solve(-211, 1000000000000000000) == 1000000000000000422


if __name__ == "__main__":
    test()
    main()
