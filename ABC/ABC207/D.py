def distance_square(x, y):
    return (x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2


def outer_product(x, y, z):
    op = (y[1] - x[1]) * (z[0] - x[0]) - (y[0] - x[0]) * (z[1] - x[1])
    return op


def solve(n, ab_list, cd_list):
    if n == 1:
        return "Yes"

    d01 = distance_square(cd_list[0], cd_list[1])
    cd_state = dict()
    for i in range(n):
        d0 = distance_square(cd_list[0], cd_list[i])
        d1 = distance_square(cd_list[1], cd_list[i])
        r1 = outer_product(cd_list[0], cd_list[1], cd_list[i])
        ddd = d0
        ddd = ddd * 1000 + d1
        ddd = ddd * 1000 + r1
        cd_state[ddd] = 1

    # print(cd_state)

    for i in range(n):
        # ab[i] -> cd[0]
        for j in range(n):
            if i == j:
                continue
            # ab[j] -> cd[1]
            if distance_square(ab_list[i], ab_list[j]) != d01:
                continue
            failed = False
            for k in range(n):
                d0 = distance_square(ab_list[i], ab_list[k])
                d1 = distance_square(ab_list[j], ab_list[k])
                r1 = outer_product(ab_list[i], ab_list[j], ab_list[k])
                ddd = d0
                ddd = ddd * 1000 + d1
                ddd = ddd * 1000 + r1
                if ddd not in cd_state.keys():
                    failed = True
                    # break
            if failed:
                continue
            else:
                return "Yes"

    return "No"


def main():
    n = int(input())
    ab_list = [tuple(map(int, input().split())) for _ in range(n)]
    cd_list = [tuple(map(int, input().split())) for _ in range(n)]
    res = solve(n, ab_list, cd_list)
    print(res)


def test():
    assert solve(3, [(0, 0), (0, 1), (1, 0)], [(2, 0), (3, 0), (3, 1)]) == "Yes"
    assert solve(3, [(1, 0), (1, 1), (3, 0)], [(-1, 0), (-1, 1), (-3, 0)]) == "No"
    assert solve(4, [(0, 0), (2, 9), (10, -2), (-6, -7)], [(0, 0), (2, 9), (10, -2), (-6, -7)]) == "Yes"


if __name__ == "__main__":
    test()
    main()
