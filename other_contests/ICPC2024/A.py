def solve(n, a_list):
    res = 0
    for a in a_list:
        if res + a <= 300:
            res += a
    return res


def main():
    res = []
    while True:
        n = int(input())
        if n == 0:
            break
        a_list = list(map(int, input().split()))
        res.append(solve(n, a_list))
    for r in res:
        print(r)


def test():
    assert solve(5, [100, 50, 200, 120, 60]) == 270
    assert solve(4, [120, 240, 180, 1]) == 300
    assert solve(2, [500, 1000]) == 0
    assert solve(6, [2, 3, 5, 7, 11, 13]) == 41


if __name__ == "__main__":
    test()
    main()
