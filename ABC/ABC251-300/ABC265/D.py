def solve(n, p, q, r, a_list):
    s = 0
    a_cum_dict = dict()
    a_cum_dict[0] = 1
    for a in a_list:
        s += a
        a_cum_dict[s] = 1

    for a in a_cum_dict.keys():
        if a + p in a_cum_dict.keys() and a + p + q in a_cum_dict.keys() and a + p + q + r in a_cum_dict.keys():
            return "Yes"
    return "No"


def main():
    n, p, q, r = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, p, q, r, a_list)
    print(res)


def test():
    assert solve(10, 5, 7, 5, [1, 3, 2, 2, 2, 3, 1, 4, 3, 2]) == "Yes"
    assert solve(9, 100, 101, 100, [31, 41, 59, 26, 53, 58, 97, 93, 23]) == "No"
    assert solve(7, 1, 1, 1, [1, 1, 1, 1, 1, 1, 1]) == "Yes"


if __name__ == "__main__":
    test()
    main()
