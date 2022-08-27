import math


def solve(a, b, c, d):
    d_ab = math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
    d_bc = math.sqrt((b[0] - c[0]) ** 2 + (b[1] - c[1]) ** 2)
    d_cd = math.sqrt((c[0] - d[0]) ** 2 + (c[1] - d[1]) ** 2)
    d_da = math.sqrt((d[0] - a[0]) ** 2 + (d[1] - a[1]) ** 2)
    d_ac = math.sqrt((a[0] - c[0]) ** 2 + (a[1] - c[1]) ** 2)
    d_bd = math.sqrt((b[0] - d[0]) ** 2 + (b[1] - d[1]) ** 2)
    # angle a
    angle_a = math.acos((d_da ** 2 + d_ab ** 2 - d_bd ** 2) / (2 * d_da * d_ab))
    angle_b = math.acos((d_ab ** 2 + d_bc ** 2 - d_ac ** 2) / (2 * d_ab * d_bc))
    angle_c = math.acos((d_bc ** 2 + d_cd ** 2 - d_bd ** 2) / (2 * d_bc * d_cd))
    angle_d = math.acos((d_cd ** 2 + d_da ** 2 - d_ac ** 2) / (2 * d_cd * d_da))

    if angle_a + angle_b + angle_c + angle_d >= 2 * math.pi - 0.0000001:
        return "Yes"
    return "No"


def main():
    a = tuple(map(int, input().split()))
    b = tuple(map(int, input().split()))
    c = tuple(map(int, input().split()))
    d = tuple(map(int, input().split()))
    res = solve(a, b, c, d)
    print(res)


def test():
    assert solve((0, 0), (1, 0), (1, 1), (0, 1)) == "Yes"
    assert solve((0, 0), (1, 1), (-1, 0), (1, -1)) == "No"


if __name__ == "__main__":
    test()
    main()
