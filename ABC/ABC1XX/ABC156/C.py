def solve(n, a_list):
    res = 100000000
    for p in range(101):
        r = sum([(a_list[i] - p) ** 2 for i in range(n)])
        if r < res:
            res = r

    return res


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(2, [1, 4]) == 5
    assert solve(7, [14, 14, 2, 13, 56, 2, 37]) == 2354


if __name__ == "__main__":
    test()
    main()
