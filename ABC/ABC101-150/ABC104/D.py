MOD = 10 ** 9 + 7


def solve(s):
    n = 1
    a = 0
    ab = 0
    abc = 0
    for c in s:
        if c == "A":
            a += n
        elif c == "B":
            ab += a
        elif c == "C":
            abc += ab
        else:
            abc = 3 * abc + ab
            ab = 3 * ab + a
            a = 3 * a + n
            n *= 3
        n %= MOD
        a %= MOD
        ab %= MOD
        abc %= MOD
        # print(a, ab, abc)
    return abc


def main():
    s = input()
    res = solve(s)
    print(res)


def test():
    assert solve("A??C") == 8
    assert solve("ABCBC") == 3
    assert solve("???") == 1
    assert solve("????") == 12
    assert solve("????C?????B??????A???????") == 979596887


if __name__ == "__main__":
    test()
    main()
