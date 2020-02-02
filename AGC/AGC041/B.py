def solve(n, m, v, p, a_list):
    a_list_s = sorted(a_list, reverse=True)
    # member
    # vote: v
    # problem: p
    base_bar = a_list_s[p - 1]
    res = p
    space = 0
    for i in range(p, n):
        if a_list_s[i] + m - base_bar < 0:
            break
        space_now = space + (a_list_s[i] + m - base_bar) * (i - p + 1)
        v_now = max(v - (n - i) - (p - 1), 0)
        if space_now >= v_now * m:
            res += 1
        space += base_bar - a_list_s[i]

    return res


def main():
    n, m, v, p = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, m, v, p, a_list)
    print(res)


def test():
    assert solve(6, 1, 2, 2, [2, 1, 1, 3, 0, 2]) == 5
    assert solve(6, 1, 5, 2, [2, 1, 1, 3, 0, 2]) == 3
    assert solve(10, 4, 8, 5, [7, 2, 3, 6, 1, 6, 5, 4, 6, 5]) == 8


if __name__ == "__main__":
    test()
    main()
