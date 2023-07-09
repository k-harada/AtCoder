def solve_sub(n, k):
    if (n - k) % 2 == 1:
        return "No"
    res_min = 0
    m = n
    while m > 0:
        res_min += m % 3
        m //= 3
    if res_min > k:
        return "No"
    return "Yes"


def solve(t, case_list):
    res = [solve_sub(n, k) for n, k in case_list]
    # print(res)
    return res


def main():
    t = int(input())
    case_list = []
    for _ in range(t):
        n, k = map(int, input().split())
        case_list.append((n, k))
    res = solve(t, case_list)
    for r in res:
        print(r)


def test():
    assert solve(4, [
        (5, 3), (17, 2), (163, 79), (1000000000000000000, 1000000000000000000)
    ]) == ["Yes", "No", "Yes", "Yes"]


if __name__ == "__main__":
    test()
    main()
