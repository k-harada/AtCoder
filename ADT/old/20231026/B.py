def solve(n, p, q, d_list):
    res = min(p, q + min(d_list))
    return res


def main():
    n, p, q = map(int, input().split())
    d_list = list(map(int, input().split()))
    res = solve(n, p, q, d_list)
    print(res)


def test():
    assert solve(3, 100, 50, [60, 20, 40]) == 70
    assert solve(3, 100, 50, [60000, 20000, 40000]) == 100


if __name__ == "__main__":
    test()
    main()
