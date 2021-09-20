def solve():
    return 0


def main():
    n, k = map(int, input().split())
    a_list = list(map(int, input().split()))
    # s = input()
    res = solve()
    print(res)
    # for r in res:
    #     print(r)


def test():
    assert solve() == 0
    assert solve() == 0
    assert solve() == 0


if __name__ == "__main__":
    test()
    main()
