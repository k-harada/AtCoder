def solve(n, a_list):
    a_list_add = [(len(str(a)), str(a)) for a in a_list]
    a_list_add_s = list(sorted(a_list_add, reverse=True))
    a_list_add_ss = list(sorted([str(a[1]) for a in a_list_add_s[:3]], reverse=True))
    return int(str(a_list_add_ss[0]) + str(a_list_add_ss[1]) + str(a_list_add_ss[2]))


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(5, [1, 4, 3, 5, 8]) == 854
    assert solve(8, [813, 921, 481, 282, 120, 900, 555, 409]) == 921900813


if __name__ == "__main__":
    test()
    main()
