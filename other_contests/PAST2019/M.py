def solve():
    return 0


def main():
    n, m = map(int, input().split())
    a_list = [0] * n
    b_list = [0] * n
    c_list = [0] * m
    d_list = [0] * m
    for i in range(n):
        a, b = map(int, input().split())
        a_list[i] = a
        b_list[i] = b
    for i in range(m):
        c, d = map(int, input().split())
        c_list[i] = c
        d_list[i] = d
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
