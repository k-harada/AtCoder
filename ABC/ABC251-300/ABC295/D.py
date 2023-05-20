def solve(s):
    v_count = [0] * 1024
    v_count[0] = 1
    v = 0
    for c in s:
        v ^= 2 ** int(c)
        v_count[v] += 1
    res = 0
    for i in range(1024):
        res += v_count[i] * (v_count[i] - 1) // 2
    # print(v_count)
    # print(res)
    return res


def main():
    s = input()
    res = solve(s)
    print(res)


def test():
    assert solve("20230322") == 4
    assert solve("0112223333444445555556666666777777778888888889999999999") == 185
    assert solve("3141592653589793238462643383279502884197169399375105820974944") == 9


if __name__ == "__main__":
    test()
    main()
