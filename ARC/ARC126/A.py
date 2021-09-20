def solve(t, case_list):
    res = []
    for n2, n3, n4 in case_list:
        # use n3 by 4
        r = 0
        c6 = n3 // 2
        if n4 >= c6:
            r += c6
            c4 = n4 - c6
            c6 = 0
        else:
            r += n4
            c6 -= n4
            c4 = 0
        # print(r, c4, c6)
        # use n3 by 2
        if c6 > 0:
            if n2 >= 2 * c6:
                r += c6
                c2 = n2 - 2 * c6
                c6 = 0
            else:
                r += n2 // 2
                c2 = n2 % 2
                c6 -= n2 // 2
        else:
            c2 = n2
        # print(r, c2, c4, c6)
        if c4 // 2 > c2:
            r += c2
            c4 -= 2 * c2
            c2 = 0
        else:
            r += c4 // 2
            c2 -= c4 // 2
            c4 = c4 % 2
        # print(r, c2, c4, c6)
        if c4 >= 1 and c2 >= 3:
            c4 -= 1
            c2 -= 3
            r += 1

        r += c2 // 5

        res.append(r)
    # print(res)
    return res


def main():
    t = int(input())
    case_list = [tuple(map(int, input().split())) for _ in range(t)]
    res = solve(t, case_list)
    for r in res:
        print(r)


def test():
    assert solve(
        5, [(3, 4, 1), (7, 0, 0), (0, 0, 7), (0, 0, 0), (1000000000000000, 1000000000000000, 1000000000000000)]
    ) == [2, 1, 0, 0, 900000000000000]


if __name__ == "__main__":
    test()
    main()
