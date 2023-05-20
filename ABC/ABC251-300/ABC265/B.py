def solve(n, m, t, a_list, xy_list):
    # simulate
    t_now = t
    j = 0
    if m > 0:
        p = xy_list[0][0] - 1
    else:
        p = n + 1
    for i in range(n - 1):
        if i == p:
            t_now += xy_list[j][1]
            j += 1
            if j < m:
                p = xy_list[j][0] - 1
            else:
                p = n + 1
        t_now -= a_list[i]
        # print(t_now)
        if t_now <= 0:
            return "No"
    return "Yes"


def main():
    n, m, t = map(int, input().split())
    a_list = list(map(int, input().split()))
    xy_list = [tuple(map(int, input().split())) for _ in range(m)]
    res = solve(n, m, t, a_list, xy_list)
    print(res)


def test():
    assert solve(4, 1, 10, [5, 7, 5], [(2, 10)]) == "Yes"
    assert solve(4, 1, 10, [10, 7, 5], [(2, 10)]) == "No"


if __name__ == "__main__":
    test()
    main()
