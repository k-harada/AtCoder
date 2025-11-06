def solve(m, s):
    res = 10 * m
    for i in range(3 * m):
        c_i = s[0][i % m]
        for j in range(3 * m):
            if i == j:
                continue
            c_j = s[1][j % m]
            if c_j != c_i:
                continue
            for k in range(3 * m):
                if k == i or k == j:
                    continue
                c_k = s[2][k % m]
                if c_k != c_i:
                    continue
                r = max([i, j, k])
                res = min(res, r)
    if res == 10 * m:
        res = -1
    return res


def main():
    m = int(input())
    s = [input() for _ in range(3)]
    res = solve(m, s)
    print(res)


def test():
    assert solve(10, [
        "1937458062",
        "8124690357",
        "2385760149"
    ]) == 6
    assert solve(20, [
        "01234567890123456789",
        "01234567890123456789",
        "01234567890123456789"
    ]) == 20
    assert solve(5, [
        "11111",
        "22222",
        "33333"
    ]) == -1
    assert solve(100, [
        "1" * 99 + "4",
        "2" * 99 + "4",
        "3" * 99 + "4"
    ]) == 299


if __name__ == "__main__":
    # test()
    main()
