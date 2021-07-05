def solve(k):
    a_mod = 0
    pow_10 = 7
    for i in range(1000000):
        a_mod += pow_10
        a_mod %= k
        if a_mod == 0:
            return i + 1
        pow_10 *= 10
        pow_10 %= k
    return -1


def main():
    k = int(input())
    res = solve(k)
    print(res)


def test():
    assert solve(101) == 4
    assert solve(2) == -1
    assert solve(999983) == 999982


if __name__ == "__main__":
    test()
    main()
