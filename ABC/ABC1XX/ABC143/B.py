def solve_b(n, d_list):
    s1 = sum(d_list)
    s2 = sum([d ** 2 for d in d_list])
    res = (s1 ** 2 - s2) // 2
    return res


def main():
    n = int(input())
    d_list = list(map(int, input().split()))
    res = solve_b(n, d_list)
    print(res)


def test():
    assert solve_b(3, [3, 1, 2]) == 11
    assert solve_b(7, [5, 0, 7, 8, 3, 3, 2]) == 312


if __name__ == "__main__":
    test()
    main()
