def solve_sub(n, p_list):
    q_list = [0] * (n + 1)
    for i, p in enumerate(p_list):
        q_list[p] = i
    res = n
    j = 0
    for i in range(1, n + 1):
        p = q_list[i]
        # print(i, p, j)
        if p < j:
            continue
        res -= (p - j)
        j = p + 1
    # print(res)
    return res


def solve(t, case_list):
    return [solve_sub(n, p_list) for n, p_list in case_list]


def main():
    t = int(input())
    case_list = []
    for _ in range(t):
        n = int(input())
        p_list = list(map(int, input().split()))
        case_list.append((n, p_list))
    res = solve(t, case_list)
    for r in res:
        print(r)


def test():
    assert solve(3, [
        (2, [2, 1]),
        (4, [1, 2, 3, 4]),
        (20, [13, 2, 7, 1, 5, 9, 3, 4, 12, 10, 15, 6, 8, 14, 20, 16, 19, 18, 11, 17])
    ]) == [1, 4, 7]


if __name__ == "__main__":
    test()
    main()
