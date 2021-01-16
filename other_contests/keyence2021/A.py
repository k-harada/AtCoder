def solve(n, a_list, b_list):
    res_list = []
    a_cum_max = []
    a_max = 0
    for a in a_list:
        a_max = max(a, a_max)
        a_cum_max.append(a_max)
    ab_max = 0
    for i, b in enumerate(b_list):
        ab_max = max(ab_max, b * a_cum_max[i])
        res_list.append(ab_max)
    return res_list


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    res_list = solve(n, a_list, b_list)
    for res in res_list:
        print(res)


def test():
    assert solve(3, [3, 2, 20], [1, 4, 1]) == [3, 12, 20]


if __name__ == "__main__":
    test()
    main()
