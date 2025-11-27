def solve(s):
    count_list = [0] * 26
    for i, c in enumerate("abcdefghijklmnopqrstuvwxyz"):
        count_list[i] = s.count(c)
    m = max(count_list)
    for i in range(26):
        if count_list[i] == m:
            return "abcdefghijklmnopqrstuvwxyz"[i]
    return "o"


def main():
    s = input()
    res = solve(s)
    print(res)


def test():
    assert solve("frequency") == "e"
    assert solve("atcoder") == "a"
    assert solve("pseudopseudohypoparathyroidism") == "o"


if __name__ == "__main__":
    test()
    main()
