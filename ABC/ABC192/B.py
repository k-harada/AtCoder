def solve(s):
    for i, c in enumerate(s):
        if i % 2 == 0 and c.lower() != c:
            return "No"
        if i % 2 == 1 and c.upper() != c:
            return "No"
    return "Yes"


def main():
    s = input()
    res = solve(s)
    print(res)


def test():
    assert solve("dIfFiCuLt") == "Yes"
    assert solve("eASY") == "No"
    assert solve("a") == "Yes"


if __name__ == "__main__":
    test()
    main()
