def solve(n, m, a_list):
    res = [0] * m
    v_list = [[] for _ in range(n + 1)]
    for i, a in enumerate(a_list):
        if a < 0:
            j0 = (- a) // (i + 1)
        else:
            j0 = 1
        v = a + (i + 1) * (j0 - 1)
        for j in range(j0, m + 1):
            v += (i + 1)
            # print(j, v)
            if 0 <= v <= n:
                v_list[v].append(j)
            elif v < 0:
                continue
            else:
                break
    # print(v_list)
    v = 0
    x_set = set(list(range(1, m + 1)))
    while len(x_set):
        for x in x_set - set(v_list[v]):
            res[x - 1] = v
        x_set = x_set.intersection(set(v_list[v]))
        v += 1
    # print(res)
    return res


def main():
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, m, a_list)
    for r in res:
        print(r)


def test():
    assert solve(3, 3, [-1, -1, -6]) == [2, 2, 0]
    assert solve(5, 6, [-2, -2, -5, -7, -15]) == [1, 3, 2, 0, 0, 0]


def test_large():
    print(solve(200000, 200000, [0] * 200000))


if __name__ == "__main__":
    test()
    main()
