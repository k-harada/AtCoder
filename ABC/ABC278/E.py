def solve(h, w, n, h_, w_, a):
    count = [0] * (n + 1)
    vi_min = [n] * (n + 1)
    vi_max = [-1] * (n + 1)
    vj_min = [n] * (n + 1)
    vj_max = [-1] * (n + 1)

    for i in range(h):
        for j in range(w):
            v = a[i][j]
            count[v] += 1
            vi_min[v] = min(i, vi_min[v])
            vi_max[v] = max(i, vi_max[v])
            vj_min[v] = min(j, vj_min[v])
            vj_max[v] = max(j, vj_max[v])

    total_count = 0
    for i in range(n + 1):
        if count[i] > 0:
            total_count += 1

    res_list = [[total_count] * (w - w_ + 1) for _ in range(h - h_ + 1)]

    for v in range(n + 1):
        if count[v] == 0:
            continue
        for i in range(h - h_ + 1):
            for j in range(w - w_ + 1):
                if i <= vi_min[v] and vi_max[v] < i + h_ and j <= vj_min[v] and vj_max[v] < j + w_:
                    res_list[i][j] -= 1
    # print(res_list)
    return [" ".join([str(a) for a in res]) for res in res_list]


def main():
    h, w, n, h_, w_ = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    res = solve(h, w, n, h_, w_, a)
    for r in res:
        print(r)


def test():
    assert solve(3, 4, 5, 2, 2, [[2, 2, 1, 1], [3, 2, 5, 3], [3, 4, 4, 3]]) == ["4 4 3", "5 3 4"]
    assert solve(5, 6, 9, 3, 4, [
        [7, 1, 5, 3, 9, 5],
        [4, 5, 4, 5, 1, 2],
        [6, 1, 6, 2, 9, 7],
        [4, 7, 1, 5, 8, 8],
        [3, 4, 3, 3, 5, 3],
    ]) == ["8 8 7", "8 9 7", "8 9 8"]


def test_large():
    print(solve(300, 300, 300, 1, 1, [list(range(1, 301)) for _ in range(300)]))


if __name__ == "__main__":
    test()
    # test_large()
    main()
