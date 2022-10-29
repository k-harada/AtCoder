def solve(n, apx_list):
    res = 10 ** 9 + 7
    for a, p, x in apx_list:
        if x > a:
            res = min(res, p)
    if res == 10 ** 9 + 7:
        return -1
    return res


def main():
    n = int(input())
    apx_list = [tuple(map(int, input().split())) for _ in range(n)]
    res = solve(n, apx_list)
    print(res)


def test():
    assert solve(3, [(3, 9, 5), (4, 8, 5), (5, 7, 5)]) == 8
    assert solve(3, [(5, 9, 5), (6, 8, 5), (7, 7, 5)]) == -1


if __name__ == "__main__":
    test()
    main()
