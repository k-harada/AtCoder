def solve(s):
    if s in ["ACE", "BDF", "CEG", "DFA", "EGB", "FAC", "GBD"]:
        return "Yes"
    else:
        return "No"


def main():
    s = input()
    res = solve(s)
    print(res)


def test():
    assert solve("ABC") == "No"
    assert solve("FAC") == "Yes"
    assert solve("XYX") == "No"


if __name__ == "__main__":
    test()
    main()
