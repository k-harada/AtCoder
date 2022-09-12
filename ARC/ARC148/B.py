def solve(n, s):

    if s == "d" * n:
        return s
    if s == "p" * n:
        return "d" * n

    first_p = 0
    for i in range(n):
        if s[i] == "p":
            first_p = i
            break

    reversed_s = ""
    for c in list(reversed(list(s))):
        if c == "d":
            reversed_s += "p"
        else:
            reversed_s += "d"

    res = "p" * n
    for j in range(first_p, n + 1):
        r = s[:first_p] + reversed_s[(n - j):(n - first_p)] + s[j:]
        # print(s[:first_p], reversed_s[(n - j):(n - first_p)], s[j:])
        if r < res:
            res = r

    return res


def main():
    n = int(input())
    s = input()
    res = solve(n, s)
    print(res)


def test():
    assert solve(6, "dpdppd") == "dddpdd"
    assert solve(3, "ddd") == "ddd"
    assert solve(11, "ddpdpdppddp") == "ddddpdpdddp"

def solve(n, s):

    if s == "d" * n:
        return s
    if s == "p" * n:
        return "d" * n

    first_p = 0
    for i in range(n):
        if s[i] == "p":
            first_p = i
            break

    reversed_s = ""
    for c in list(reversed(list(s))):
        if c == "d":
            reversed_s += "p"
        else:
            reversed_s += "d"

    res = "p" * n
    for j in range(first_p, n + 1):
        r = s[:first_p] + reversed_s[(n - j):(n - first_p)] + s[j:]
        # print(s[:first_p], reversed_s[(n - j):(n - first_p)], s[j:])
        if r < res:
            res = r

    return res


def main():
    n = int(input())
    s = input()
    res = solve(n, s)
    print(res)


def test():
    assert solve(6, "dpdppd") == "dddpdd"
    assert solve(3, "ddd") == "ddd"
    assert solve(11, "ddpdpdppddp") == "ddddpdpdddp"


def test_large():
    print(solve(5000, "dp" * 2500))


if __name__ == "__main__":
    test()
    # test_large()
    main()
