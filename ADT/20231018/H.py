import math
from decimal import Decimal


def solve(n, xy_list):

    # 角度でソートする
    angle_list = []
    for i in range(n):
        x, y = xy_list[i]
        angle_1 = Decimal(y - 1) / Decimal(x)
        if x > 1:
            angle_2 = Decimal(y) / Decimal(x - 1)
        else:
            angle_2 = math.inf
        angle_list.append((angle_1, angle_2))
    angle_list_s = list(sorted(angle_list, key=lambda xy: xy[1]))

    right_max = -1
    res = 0
    for left, right in angle_list_s:
        if left >= right_max:
            res += 1
            right_max = right

    return res


def main():
    n = int(input())
    xy_list = [tuple(map(int, input().split())) for _ in range(n)]
    res = solve(n, xy_list)
    print(res)


def test():
    assert solve(3, [(1, 1), (2, 1), (1, 2)]) == 2
    assert solve(10, [
        (414598724, 87552841),
        (252911401, 309688555),
        (623249116, 421714323),
        (605059493, 227199170),
        (410455266, 373748111),
        (861647548, 916369023),
        (527772558, 682124751),
        (356101507, 249887028),
        (292258775, 110762985),
        (850583108, 796044319),
    ]) == 10


if __name__ == "__main__":
    test()
    main()
