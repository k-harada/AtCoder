def solve(h, a):
    if h % a == 0:
        return h // a
    else:
        return h // a + 1


def main():
    h, a = map(int, input().split())
    res = solve(h, a)
    print(res)
    # for r in res:
    #     print(r)


def test():
    assert solve(10, 4) == 3
    assert solve(1, 10000) == 1
    assert solve(10000, 1) == 10000


if __name__ == "__main__":
    test()
    main()
