def solve(h, w, m, hw_list):
    h_count = [0] * (h + 1)
    w_count = [0] * (w + 1)
    for h_, w_ in hw_list:
        h_count[h_] += 1
        w_count[w_] += 1

    h_max = max(h_count)
    w_max = max(w_count)
    res = h_max + w_max

    h_max_count = 0
    w_max_count = 0
    for i in range(h + 1):
        if h_count[i] == h_max:
            h_max_count += 1
    for j in range(w + 1):
        if w_count[j] == w_max:
            w_max_count += 1

    max_count = h_max_count * w_max_count
    max_count_cross = 0
    for h_, w_ in hw_list:
        if h_count[h_] == h_max and w_count[w_] == w_max:
            max_count_cross += 1

    if max_count_cross == max_count:
        return res - 1
    else:
        return res


def main():
    h, w, m = map(int, input().split())
    hw_list = []
    for _ in range(m):
        hw_list.append(list(map(int, input().split())))
    res = solve(h, w, m, hw_list)
    print(res)


def test():
    assert solve(2, 3, 3, [[2, 2], [1, 1], [1, 3]]) == 3
    assert solve(3, 3, 4, [[3, 3], [3, 1], [1, 1], [1, 2]]) == 3
    assert solve(5, 5, 10, [[2, 5], [4, 3], [2, 3], [5, 5], [2, 2], [5, 4], [5, 3], [5, 1], [3, 5], [1, 4]]) == 6


if __name__ == "__main__":
    test()
    main()
