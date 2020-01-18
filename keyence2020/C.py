def solve(n, k, s):
    if s < 10 ** 9:
        res_list = [s] * k + [s + 1] * (n - k)
    else:
        res_list = [s] * k + [s - 1] * (n - k)
    res = " ".join([str(a) for a in res_list])
    return res


def main():
    n, k, s = map(int, input().split())
    res = solve(n, k, s)
    print(res)


def test():
    assert solve(4, 2, 3) == "3 3 4 4"
    assert solve(5, 3, 100) == "100 100 100 101 101"
    assert solve(5, 3, 1) == "1 1 1 2 2"


if __name__ == "__main__":
    test()
    main()
