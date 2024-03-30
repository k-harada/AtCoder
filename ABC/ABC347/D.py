def solve(a, b, c):
    bit_list = []
    x = c
    for i in range(60):
        bit_list.append(x & 1)
        x //= 2
    d = sum(bit_list)
    if d > a + b:
        return "-1"
    elif d < max(a - b, b - a):
        return "-1"
    elif (a + b - d) % 2 == 1:
        return "-1"
    rr = (a + b - d) // 2
    if rr > 60 - d:
        return "-1"
    aa = a - rr
    bb = b - rr
    p = 0
    q = 0
    for i in range(60):
        if bit_list[i] == 1:
            if aa > 0:
                p += 2 ** i
                aa -= 1
            else:
                q += 2 ** i
                bb -= 1
    for i in range(60):
        if bit_list[i] == 0:
            if rr > 0:
                p += 2 ** i
                q += 2 ** i
                rr -= 1
    assert p ^ q == c
    # print(p, q)
    return f"{p} {q}"


def main():
    a, b, c = map(int, input().split())
    res = solve(a, b, c)
    print(res)


def test():
    assert solve(3, 4, 7) == "25 30"
    assert solve(34, 56, 998244353) == "-1"
    assert solve(39, 47, 530423800524412070) == "10008154762903551 540431955281603417"


if __name__ == "__main__":
    test()
    main()
