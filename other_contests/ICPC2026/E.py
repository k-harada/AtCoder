def solve(n, ab_list):
    sake_list = []
    gem_min = 10 ** 10
    gem_cnt = 0
    for a, b in ab_list:
        if b > 0:
            gem_cnt += b
            if a < gem_min:
                sake_list.append(gem_min)
                gem_min = a
            else:
                sake_list.append(a)
        else:
            sake_list.append(a)
    if gem_cnt == 0:
        res = sum(sake_list)
    else:
        res = gem_min
        to_buy = max(0, n - 1 - gem_cnt)
        # print(res, to_buy)
        sake_list_s = list(sorted(sake_list))
        res += sum(sake_list_s[:to_buy])
    # print(res)
    return res


def main():
    n = int(input())
    ab_list = [tuple(map(int, input().split())) for _ in range(n)]
    res = solve(n, ab_list)
    print(res)


def test():
    assert solve(4, [(400, 1), (500, 0), (600, 1), (800, 2)]) == 400
    assert solve(5, [(1540, 0), (1430, 0), (1320, 0), (1210, 0), (1100, 0)]) == 6600
    assert solve(20, [
        (861, 0), (901, 0), (955, 1), (602, 1), (882, 1),
        (188, 1), (817, 0), (932, 2), (669, 0), (621, 2),
        (276, 0), (668, 0), (825, 1), (834, 1), (341, 2),
        (545, 0), (218, 0), (939, 0), (179, 1), (587, 1)
    ]) == 1747


if __name__ == "__main__":
    test()
    main()
