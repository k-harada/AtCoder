def solve(le, n1, n2, vl_1, vl_2):
    j1 = 0
    j2 = 0
    v1 = vl_1[0][0]
    v2 = vl_2[0][0]
    x1 = 0
    x2 = 0
    x = 0
    vl_1.append((-1, 1))
    vl_2.append((-2, 1))
    res = 0
    while min(x1, x2) < le:
        if x1 < le:
            next_x1 = x1 + vl_1[j1][1]
        else:
            next_x1 = le
        if x2 < le:
            next_x2 = x2 + vl_2[j2][1]
        else:
            next_x2 = le
        # print(x1, x2, j1, j2, v1, v2, le)
        if next_x1 < next_x2 or (next_x1 == next_x2 and x1 <= x2):
            if v1 == v2:
                res += (next_x1 - x)
            x = next_x1
            x1 = next_x1
            j1 += 1
            v1 = vl_1[j1][0]
        else:
            if v1 == v2:
                res += (next_x2 - x)
            x = next_x2
            x2 = next_x2
            j2 += 1
            v2 = vl_2[j2][0]
        # print(res)
    return res


def main():
    le, n1, n2 = map(int, input().split())
    vl_1 = [tuple(map(int, input().split())) for _ in range(n1)]
    vl_2 = [tuple(map(int, input().split())) for _ in range(n2)]
    res = solve(le, n1, n2, vl_1, vl_2)
    print(res)


def test():
    assert solve(8, 4, 3, [
        (1, 2), (3, 2), (2, 3), (3, 1)
    ], [
        (1, 4), (2, 1), (3, 3)
    ]) == 4
    assert solve(10000000000, 1, 1, [
        (1, 10000000000)
    ], [
        (1, 10000000000)
    ]) == 10000000000
    assert solve(1000, 4, 7, [
        (19, 79),
        (33, 463),
        (19, 178),
        (33, 280)
    ], [
        (19, 255),
        (33, 92),
        (34, 25),
        (19, 96),
        (12, 11),
        (19, 490),
        (33, 31)
    ]) == 380


if __name__ == "__main__":
    test()
    main()
