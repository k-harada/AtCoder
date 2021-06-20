def solve(n, a_list):
    res = n * (n + 1) // 2
    v_dict = dict()
    for a in a_list:
        if a not in v_dict.keys():
            v_dict[a] = 1
        else:
            v_dict[a] += 1
    for v in v_dict.values():
        res -= v * (v + 1) // 2
    return res


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(3, [1, 7, 1]) == 2
    assert solve(10, [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]) == 45
    assert solve(20, [7, 8, 1, 1, 4, 9, 9, 6, 8, 2, 4, 1, 1, 9, 5, 5, 5, 3, 6, 4]) == 173


def test_large():
    print(solve(300000, [1] * 300000))
    print(solve(300000, list(range(300000))))


if __name__ == "__main__":
    test()
    # test_large()
    main()
