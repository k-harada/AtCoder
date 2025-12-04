def solve(h, w, n, ab_list):
    a_count = dict()
    b_count = dict()

    for a, b in ab_list:
        if a not in a_count.keys():
            a_count[a] = 1
        else:
            a_count[a] += 1
        if b not in b_count.keys():
            b_count[b] = 1
        else:
            b_count[b] += 1

    a_res = [0]
    b_res = [0]
    for a in sorted(a_count.keys()):
        a_res.append(a)

    for b in sorted(b_count.keys()):
        b_res.append(b)

    a_map = dict()
    b_map = dict()
    # print(a_res)
    # print(b_res)

    for i, a in enumerate(a_res):
        a_map[a] = i
    for i, b in enumerate(b_res):
        b_map[b] = i
    # print(a_map)
    # print(b_map)
    res = []

    for a, b in ab_list:
        a_ = a_map[a]
        b_ = b_map[b]
        res.append(f"{a_} {b_}")
    # print(res)
    return res


def main():
    h, w, n = map(int, input().split())
    ab_list = [tuple(map(int, input().split())) for _ in range(n)]
    res = solve(h, w, n, ab_list)
    for r in res:
        print(r)


def test():
    assert solve(4, 5, 2, [(3, 2), (2, 5)]) == ["2 1", "1 2"]
    assert solve(1000000000, 1000000000, 10, [
        (1, 1),
        (10, 10),
        (100, 100),
        (1000, 1000),
        (10000, 10000),
        (100000, 100000),
        (1000000, 1000000),
        (10000000, 10000000),
        (100000000, 100000000),
        (1000000000, 1000000000)
    ]) == ["1 1", "2 2", "3 3", "4 4", "5 5", "6 6", "7 7", "8 8", "9 9", "10 10"]


if __name__ == "__main__":
    test()
    main()
