def solve(n, m, s):
    # o---x or x---o
    # o---o
    # x---x
    # がそれぞれ長さいくつが何個あるか数える
    type_0 = [0] * (n + 1)
    type_1 = [0] * (n + 1)
    type_2 = [0] * (n + 1)
    left = "x"
    c = 0
    res = 0
    xc = 0
    for i in range(n + 1):
        if i < n:
            a = s[i]
            if a == "x":
                xc += 1
        else:
            a = "x"
        if a == "o":
            res += 1
        if a == "-":
            c += 1
        else:
            if a == "x" and left == "x":
                type_2[c] += 1
            elif a == "o" and left == "o":
                type_1[c] += 1
            else:
                type_0[c] += 1
            c = 0
            left = a
    # そもそも休み
    res += type_1[1]
    # print(res)
    # print(type_0)
    # print(type_1)
    # print(type_2)
    # 貪欲
    mm = m
    for i in range(3, n + 1, 2):
        d = min(mm // (i // 2), type_1[i])
        res += i * d
        mm -= d * (i // 2)
        if d < type_1[i]:
            res += 2 * mm
            mm = 0
            break
    # 2倍増えるところ
    twos = 0
    for i in range(2, n + 1, 2):
        twos += type_1[i] * (i // 2)
    for i in range(n + 1):
        twos += type_0[i] * (i // 2)
    # print(twos)

    if mm > twos:
        res += 2 * twos
        mm -= twos
    else:
        res += 2 * mm
        mm = 0

    # 2倍弱増えるところ
    for i in range(n, 2, -1):
        d = min(mm // ((i + 1) // 2), type_2[i])
        if i % 2 == 1:
            res += i * d
        else:
            res += (i - 1) * d
        mm -= d * ((i + 1) // 2)
        if d < type_2[i] and mm > 0:
            res += 2 * mm - 1
            mm = 0
            break

    # それでも余った場合
    res_max = n - xc
    res = min(res + mm, res_max)
    # print(res)
    return res


def main():
    n, m = map(int, input().split())
    s = input()
    res = solve(n, m, s)
    print(res)


def test():
    assert solve(8, 2, "x-o----x") == 5
    assert solve(20, 5, "xo--x-o--o--------ox") == 14
    assert solve(5, 0, "xo-ox") == 3
    assert solve(20, 20, "xo--x-o--o--------ox") == 17
    assert solve(5, 5, "xo-ox") == 3
    assert solve(6, 4, "------") == 6
    assert solve(6, 3, "------") == 5
    assert solve(6, 2, "------") == 3
    assert solve(6, 1, "------") == 1
    assert solve(6, 0, "------") == 0


if __name__ == "__main__":
    test()
    main()
