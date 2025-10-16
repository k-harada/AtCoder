def solve(n, x, m):
    count = [0] * m
    value = [0] * m
    v = x % m
    count[v] = 1
    value[v] = x
    c = 1
    res = x
    while c < n:
        v = (v * v) % m
        # print(v)
        res += v
        c += 1
        if count[v] > 0:
            cc = (n - c) // (c - count[v])
            c += cc * (c - count[v])
            res += cc * (res - value[v])
        else:
            count[v] = c
            value[v] = res
        # print(c, v, res)
    return res


def main():
    n, x, m = map(int, input().split())
    res = solve(n, x, m)
    print(res)


def test():
    assert solve(6, 2, 1001) == 1369
    assert solve(1000, 2, 16) == 6
    assert solve(10000000000, 10, 99959) == 492443256176507


if __name__ == "__main__":
    test()
    main()
