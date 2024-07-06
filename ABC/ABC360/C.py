def solve(n, a_list, w_list):
    max_list = [0] * (n + 1)
    s = 0
    for a, w in zip(a_list, w_list):
        s += w
        max_list[a] = max(max_list[a], w)
    res = s - sum(max_list)
    return res


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    w_list = list(map(int, input().split()))
    res = solve(n, a_list, w_list)
    print(res)


def test():
    assert solve(5, [2, 2, 3, 3, 5], [33, 40, 2, 12, 16]) == 35
    assert solve(12, [3, 6, 7, 4, 12, 4, 8, 11, 11, 1, 8, 11], [
        3925, 9785, 9752, 3587, 4013, 1117, 3937, 7045, 6437, 6208, 3391, 6309
    ]) == 17254
    assert solve(5, [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]) == 0


if __name__ == "__main__":
    test()
    main()
