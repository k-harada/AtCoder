def solve(n, m, ab_list, xy_list):
    a_list = []
    b_list = []
    same_list = []
    xy_list_s = list(set(xy_list))
    # print(xy_list_s)
    for x, y in xy_list:
        if x == y:
            same_list.append(x - 1)
    for i, (a, b) in enumerate(ab_list):
        if i in same_list:
            a, b = max(a, b), min(a, b)
        a_list.append(a)
        b_list.append(b)
    res = a_list.copy()
    means = [(a + b) / 2 for a, b in zip(a_list, b_list)]
    # print(means)
    # print(a_list)
    # print(b_list)
    p = len(xy_list_s)
    for _ in range(p):
        change = 0
        for x, y in xy_list_s:
            if res[x - 1] + res[y - 1] + 0.1 < means[x - 1] + means[y - 1]:
                res[x - 1] = means[x - 1]
                res[y - 1] = means[y - 1]
                change += 1
        if change == 0:
            break
    return sum(res)


def main():
    n, m = map(int, input().split())
    ab_list = [tuple(map(int, input().split())) for _ in range(n)]
    xy_list = [tuple(map(int, input().split())) for _ in range(m)]
    res = solve(n, m, ab_list, xy_list)
    print(res)


def test():
    assert solve(3, 1, [(3, 10), (10, 6), (5, 2)], [(1, 2)]) == 19.5
    assert solve(1, 3, [(5, 100)], [(1, 1), (1, 1), (1, 1)]) == 100.0


if __name__ == "__main__":
    test()
    main()
