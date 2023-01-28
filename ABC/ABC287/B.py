def solve(n, m, s_list, t_list):
    int_map = [0] * 1000
    for t in t_list:
        int_map[int(t)] = 1
    res = 0
    for s in s_list:
        if int_map[int(s[-3:])] == 1:
            res += 1
    return res


def main():
    n, m = map(int, input().split())
    s_list = [input() for _ in range(n)]
    t_list = [input() for _ in range(m)]
    res = solve(n, m, s_list, t_list)
    print(res)


def test():
    assert solve(3, 3, ["142857", "004159", "071028"], ["159", "287", "857"]) == 2


if __name__ == "__main__":
    test()
    main()
