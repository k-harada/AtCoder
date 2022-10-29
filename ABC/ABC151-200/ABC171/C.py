def solve(n):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    s_list = []
    m = n
    while m > 0:
        m = m - 1
        s_list.append(alphabet[m % 26])
        m = m // 26
    return "".join(reversed(s_list))


def main():
    n = int(input())
    res = solve(n)
    print(res)


def test():
    assert solve(2) == "b"
    assert solve(27) == "aa"
    assert solve(123456789) == "jjddja"


if __name__ == "__main__":
    test()
    main()
