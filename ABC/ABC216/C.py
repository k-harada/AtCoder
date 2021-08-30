def solve(n):
    res = ["A"]
    for c in bin(n)[3:]:
        res.append("B")
        if c == '1':
            res.append("A")

    return "".join(res)


def main():
    n = int(input())
    res = solve(n)
    print(res)


def test():
    assert solve(5) == "ABBA"
    assert solve(14) == "ABABAB"


if __name__ == "__main__":
    test()
    main()
