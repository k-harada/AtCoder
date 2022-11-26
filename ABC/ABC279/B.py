def solve(s, t):
    m = len(t)
    for i in range(len(s)):
        if s[i:(i + m)] == t:
            return "Yes"
    return "No"


def main():
    s = input()
    t = input()
    res = solve(s, t)
    print(res)


def test():
    assert solve("voltage", "tag") == "Yes"
    assert solve("atcoder", "ace") == "No"
    assert solve("gorilla", "gorillagorillagorilla") == "No"
    assert solve("toyotasystems", "toyotasystems") == "Yes"


if __name__ == "__main__":
    test()
    main()
