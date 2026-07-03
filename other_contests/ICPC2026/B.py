def solve(n, d, x_list):
    res = 0
    t = - 2 * d
    for x in x_list:
        if abs(x - t) > d:
            res += 1
            t = x + d
    return res


def main():
    n, d = map(int, input().split())
    x_list = list(map(int, input().split()))
    res = solve(n, d, x_list)
    print(res)


def test():
    assert solve(3, 5, [10, 20, 40]) == 2
    assert solve(9, 1, [0, 1, 2, 3, 4, 5, 6, 7, 8]) == 3
    assert solve(2, 300, [123, 724]) == 2
    assert solve(1, 100000000, [100000000]) == 1



if __name__ == "__main__":
    test()
    main()
