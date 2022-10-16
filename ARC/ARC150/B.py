def solve_sub_small(a, b):
    # b = a * q + r
    res = a
    for i in range(a):
        p = a + i
        r = b % p
        if r == 0:
            res = min(res, i)
        else:
            res = min(res, p - r + i)
    return res


def solve_sub_large(a, b):
    # b = a * q + r
    q0 = b // a
    r = b % a
    if r == 0:
        return 0
    else:
        q0 += 1
    res = a - r
    for q in range(1, q0 + 1):
        if b % q == 0:
            b0 = b
        else:
            b0 = b + (q - b % q)
        a0 = b0 // q
        if a0 < a:
            a0 = a
            b0 = a * q
        res = min(res, a0 + b0 - a - b)

    return res


def solve(t, ab_list):
    res = []
    for a, b in ab_list:
        if a >= b:
            res.append(a - b)
        elif a < 30000:
            res.append(solve_sub_small(a, b))
        else:
            res.append(solve_sub_large(a, b))
    # print(res)
    return res


def main():
    t = int(input())
    ab_list = [tuple(map(int, input().split())) for _ in range(t)]
    res = solve(t, ab_list)
    for r in res:
        print(r)


def test():
    assert solve(5, [(11, 23), (8, 16), (4394, 993298361), (95392025, 569922442), (8399283, 10293)]) == [
        2, 0, 65, 2429708, 8388990
    ]


if __name__ == "__main__":
    test()
    main()
