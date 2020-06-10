def solve(a, r, n):
    # r ** n
    res = r
    k = 1
    while k * 2 <= n - 1:
        res = res * res
        k *= 2
        if res > 10 ** 9:
            return 'large'
    res = a * pow(r, n - 1)
    if res > 10 ** 9:
        return 'large'
    return res


def main():
    a, r, n = map(int, input().split())
    res = solve(a, r, n)
    print(res)


def test():
    assert solve(2, 3, 4) == 54
    assert solve(4, 3, 21) == 'large'
    assert solve(12, 34, 5) == 16036032


if __name__ == "__main__":
    test()
    main()
