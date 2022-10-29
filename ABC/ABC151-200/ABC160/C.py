def solve(k, n, a_list):
    res = a_list[n - 1] - a_list[0]
    a_list_s = list(sorted(a_list))
    for i in range(n - 1):
        res_a = k - (a_list_s[i + 1] - a_list_s[i])
        if res_a < res:
            res = res_a
    return res


def main():
    k, n = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(k, n, a_list)
    print(res)


def test():
    assert solve(20, 3, [5, 10, 15]) == 10
    assert solve(20, 3, [0, 5, 15]) == 10


if __name__ == "__main__":
    test()
    main()
