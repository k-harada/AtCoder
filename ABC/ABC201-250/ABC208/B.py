def solve(p):
    coins = [1]
    for i in range(2, 11):
        j = coins[-1] * i
        coins.append(j)
    res = 0
    q = p
    for c in reversed(coins):
        res += q // c
        q = q % c
    return res


def main():
    p = int(input())
    res = solve(p)
    print(res)


def test():
    assert solve(9) == 3
    assert solve(119) == 10
    assert solve(10000000) == 24


if __name__ == "__main__":
    test()
    main()
