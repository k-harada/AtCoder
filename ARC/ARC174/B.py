def solve_sub(a_list, p_list):
    needs = 2 * a_list[0] + a_list[1] - a_list[3] - 2 * a_list[4]
    # print(needs)
    if needs <= 0:
        return 0
    if 2 * p_list[3] <= p_list[4]:
        return needs * p_list[3]
    elif p_list[3] <= p_list[4]:
        return (needs // 2) * p_list[4] + (needs % 2) * p_list[3]
    else:
        return (needs // 2) * p_list[4] + (needs % 2) * p_list[4]


def solve(t, case_list):
    res = [solve_sub(a, p) for a, p in case_list]
    # print(res)
    return res


def main():
    t = int(input())
    case_list = []
    for _ in range(t):
        a = list(map(int, input().split()))
        p = list(map(int, input().split()))
        case_list.append((a, p))
    res = solve(t, case_list)
    for r in res:
        print(r)


def test():
    assert solve(6, [
        ([1, 0, 1, 0, 0], [1, 2, 3, 4, 5]),
        ([0, 2, 2, 0, 0], [1, 1, 1, 1, 5]),
        ([0, 1, 2, 0, 0], [1, 1, 1, 5, 3]),
        ([1, 1, 1, 0, 0], [1, 1, 1, 1, 1]),
        ([0, 0, 0, 0, 1], [1, 1, 1, 1, 1]),
        ([100000000, 100000000, 100000000, 0, 0], [100000000, 100000000, 100000000, 100000000, 100000000]),
    ]) == [5, 2, 3, 2, 0, 15000000000000000]


if __name__ == "__main__":
    test()
    main()
